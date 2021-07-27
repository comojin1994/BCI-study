import torch
import torch.nn as nn
from torchsummary import summary
import numpy as np
import torchaudio
import torchaudio.transforms as AT
import torch.nn.functional as F
import math


class EEGGram(nn.Module):
    def __init__(self,
                 n_fft: int,
                 temporal_size: int):
        super(EEGGram, self).__init__()

        # TODO
        '''
        Conv -> Depthwise conv: 독립적으로 시간정보 추출
        pointwise conv 추가: 마지막에 시간방향으로 정보를 섞기 위해
        '''

        # 처음 커널  크기는 input의 0.01배
        self.temporal_size = temporal_size
        kernel_size = math.ceil(temporal_size * 0.01)
        output_depth = (n_fft // 2) + 1 # 255 - (n_fft // 2)
        
        self.conv_1 = nn.Conv2d(1, 16, kernel_size=[1, kernel_size], padding='same')
        self.bn_1 = nn.InstanceNorm2d(16, affine=True)
        self.pool_1 = nn.MaxPool2d(kernel_size=[1, 2], stride=[1, 2], ceil_mode=True)
        
        self.conv_2 = nn.Conv2d(16, 32, kernel_size=[1, kernel_size // 2], padding='same')
        self.bn_2 = nn.InstanceNorm2d(32, affine=True)
        self.pool_2 = nn.MaxPool2d(kernel_size=[1, 2], stride=[1, 2], ceil_mode=True)
        
        last_kernel_size, padding_size, pooling_size = self.get_padding_size()
        self.conv_3 = nn.Conv2d(32, output_depth, kernel_size=[1, last_kernel_size], padding=[0, padding_size])
        self.bn_3 = nn.InstanceNorm2d(output_depth, affine=True)
        self.pool_3 = nn.MaxPool2d(kernel_size=[1, pooling_size], stride=[1, pooling_size], ceil_mode=True)
        
        
    def forward(self, x):
        x = self.conv_1(x)
        x = self.bn_1(x)
        x = F.relu(x)
        x = self.pool_1(x)

        x = self.conv_2(x)
        x = self.bn_2(x)
        x = F.relu(x)
        x = self.pool_2(x)
        
        x = self.conv_3(x)
        x = self.bn_3(x)
        x = F.relu(x)
        x = self.pool_3(x)
        
        return x
    
    
    def get_padding_size(self):
        '''
        마지막 convolution layer의 크기를 맞춰주기 위한 function
        '''
        input_size = math.ceil(math.ceil(self.temporal_size / 2) / 2)
        spectrogram_size = 1 + self.temporal_size // math.ceil(self.temporal_size * 0.01)
        scale_ratio = math.ceil(input_size / spectrogram_size) # pooling_size
        output_size = scale_ratio * spectrogram_size

        kernel_size = math.ceil(self.temporal_size * 0.01) // 4
        if (output_size - input_size - 1 + kernel_size) % 2 != 0:
            kernel_size += 1

        padding_size = (output_size - input_size - 1 + kernel_size) // 2
        return kernel_size, padding_size, scale_ratio


class EEGPANNs(nn.Module):
    def __init__(self,
                 temporal_size: int,
                 num_channels: int,
                 is_gap: bool = False,
                 **kwargs):
        super(EEGPANNs, self).__init__()
        
        self.is_gap = is_gap
        
        n_fft = kwargs['n_fft']
        self.AE_mode = kwargs['AE_mode']
        self.use_EEGGram = kwargs['use_EEGGram']
        self.mask_ratio = kwargs['mask_ratio']

        win_length = int(np.ceil(temporal_size * 0.025))
        hop_length = int(np.ceil(temporal_size * 0.01))
        dropout_rate = 0.5

        self.spectrogram = nn.Sequential(
            AT.Spectrogram(
                n_fft=n_fft,
                win_length=win_length,
                hop_length=hop_length,
                normalized=False
            ),
        )

        mask_ratio = self.mask_ratio # 0.01, 0.3, 1000.
        mask_size = int((temporal_size // hop_length + 1) * mask_ratio)
        self.masking = AT.TimeMasking(time_mask_param=mask_size)

        self.EEGGrame = EEGGram(n_fft=n_fft, temporal_size=temporal_size)

        self.block_1 = nn.Sequential(
            nn.Conv2d(2 * ((n_fft // 2) + 1), 512, kernel_size=[1, 3], padding='same') if self.use_EEGGram
             else nn.Conv2d((n_fft // 2) + 1, 512, kernel_size=[1, 3], padding='same'),
            nn.InstanceNorm2d(512, affine=True),
            nn.Conv2d(512, 512, kernel_size=[num_channels, 1]),
            nn.InstanceNorm2d(512, affine=True),
            nn.ELU(),
            nn.AvgPool2d(kernel_size=[1, 4], stride=[1, 4]),
            nn.Dropout2d(dropout_rate)
        )

        self.block_2 = nn.Sequential(
            nn.Conv2d(512, 1024, kernel_size=[1, 3], padding='same', groups=512),
            nn.InstanceNorm2d(1024, affine=True),
            nn.Conv2d(1024, 1024, kernel_size=[1, 1]),
            nn.InstanceNorm2d(1024, affine=True),
            nn.ELU(),
            nn.AvgPool2d(kernel_size=[1, 8], stride=[1, 8]),
            nn.Dropout2d(dropout_rate)
        )
        
        if self.is_gap:
            self.gap = nn.AdaptiveAvgPool2d(1)

        
    def forward(self, x):
        x_1 = self.preprocess(x)
        
        if self.use_EEGGram:
            x_2 = self.EEGGrame(x)
            x1 = torch.cat((x_1, x_2), dim=1)
        else:
            x1 = x_1
        
        x2 = self.block_1(x1)
        x = self.block_2(x2)
        
        if self.is_gap:
            x = self.gap(x)

        if self.AE_mode: return x, x2, x1
        else: return x

    
    def preprocess(self, x):
        if x.shape[0] > 1:
            x = torch.squeeze(x)
        else:
            x = torch.squeeze(x)
            x = torch.reshape(x, (1, *x.shape))

        x = self.spectrogram(x)
        x = F.normalize(x, dim=1)
        x = self.masking(x)
        x = x.permute(0, 2, 1, 3)
        return x
