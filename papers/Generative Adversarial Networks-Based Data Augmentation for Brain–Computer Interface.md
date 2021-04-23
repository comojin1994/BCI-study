# Generative Adversarial Networks-Based Data Augmentation for Brain–Computer Interface

1. Conference or journal (Quantile): IEEE Transactions on Neural Networks and Learning Systems (Q1, 3%)
2. Year : 2020
3. 1st author : Fatemeh Fahimi
4. Professor : Cuntai Guan
5. Univ.: NTU

## Goal

    * Proposal of a framework based on the deep convolutional generative adversarial networks (DCGANs) for generating artificial EEG signal data in order to improve the performance of a classification

## Contributions

    * Suggestion of the novel framework based on GANs for generating artificial EEG signal data
    * Improvement of the classification performance with generated signal data

## Methods

    * Task
    	* Goal: the detection of subject’s movement intention
    	* Main task: right hand movement
    * Experiment conditions
    	1. Focused attention condition
    	2. Diverted attention condition
    * Dataset
    	* 14 subjects (40 trials / subject)
    	* 62 electrodes
    	* Sampling rate: 1200 Hz -> 250 Hz
    	* Preprocessing
    		* 0.01~100 Hz bandpass filter, 60 Hz notch filter
    		* ICA, ASR
    		* 0.5 Hz high pass filter
    		* Classification between intentional and unintentional movements using EMG threshold
    		* Segmentation of the EEG signals into MI and rest class
    * Baseline feature extraction & classification model
    	* Slow Cortical Potentials (SCP)-LDA
    	* End-to-end DCNN
    		* LOO / adaptive method
    * Baseline Generation model
    	* Variational Auto-Encoders (VAE)
    	* Segmentation and Recombination (S&R)
    * Use of DCGAN to generate EEG signals
    	* Use of label smoothing to improve the performance
    	* Inputs: noise & subject-specific feature vector
    		* Subject-specific feature vector
    			* Use of the pertained LOO models to extract feature vector
    			* Use of the output of the first fully connected layer
    	* Concatenation with the first half of the target subject’s samples
    * Methods of evaluating quality of the generated samples
    	* GAN-test
    	* KL divergence
    	* Visualization
    * Methods of evaluating generalizability of the proposed method

## Experiments

## Results

    * Improvement of the classification performance with generated signal data
    * Achievement in high score in GAN-test
    * Similar KL divergence results between the real data and between generated data
    * Visualization with t-SNE and spectrogram
    * Improvement of classification performance through the proposed method in another dataset

## Discussion

    * DCGANs’ superior performance compared to S&R
    * Provision of new information about unseen samples through the artificial samples
    * Reduction of data acquisition time

## Limitations

    * 일상생활속 노이즈에 대해 강건하도록 실험을 설계했지만 노이즈 제거를 위해 여러 기법 사용한 것 -> 선택적 노이즈
    * 0.01~100 Hz bandpass filter + 0.5 highpass filter 랑 0.5~100 Hz 랑 차이점 #질문
    * 데이터가 단순히 많아졌기 때문에 정확도 향상 #질문#
    * KL divergence 해석 및 평가에 대한 기주 #질문
    * rest와 비교는 치트키임

#BCI 논문리뷰#
