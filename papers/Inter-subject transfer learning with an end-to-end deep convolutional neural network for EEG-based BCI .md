# Inter-subject transfer learning with an end-to-end deep convolutional neural network for EEG-based BCI

1. Conference or journal (Quartile): Journal of Neural Engineering (Q1, 17%)
2. Year : 2019
3. 1st author : Fatemeh Fahimi
4. Professor : Cuntai Guan
5. Univ.: NTU

## Goal

    * Proposal of framework based on the CNNs to detect the attentive mental state from single-channel raw EEG data

## Contributions

    * Development of an end-to-end network in order to efficiently learn from raw EEG data
    * Suggestion of the classification strategy with inter-subject transfer learning techniques
    * Visualization of outcomes to interpret the features learned through the CNNs

## Methods

    * Dataset
    	* 120 healthy subjects with Stroop color test (frontal area)
    * Data preprocessing
    	* 2 s sliding window with 50 % overlapping
    	* Max 100 mv amplitude
    	* above 0.5 Hz
    * Input representation
    	* Raw EEG with default data preprocessing
    	* Raw EEG with default data preprocessing + 0.5-40 Hz band-pass filter
    	* Raw EEG with default data preprocessing + classical bands
    * Architecture of model

[image:3D519519-B3FC-480D-AE90-88DC74AC1030-926-000001527F7FE47B/스크린샷 2021-03-24 오전 9.35.23.png]

## Experiments

## Results

    * Single channel with baseline
    	* Baseline 1
    		* Data preprocessing: 0.5~30
    		* Feature extractor: FFT
    		* Classifier: SVM
    		* Acc: 67.9 %
    	* Baseline 2
    		* Data preprocessing: DR3 (Chebyshev type II)
    		* Feature: band powers (mean of the squared values)
    		* Classifier: LDA
    		* Acc: 68.23 %
    * Single channel with Deep CNN
    	* Deep CNN with LOO
    		* Acc: 76.2 %, 75.07 %, 76.68 %
    	* Deep CNN with subject adaptation
    		* Re-training on a small sample size of a new subject’s data
    		* Acc: 79.26 %, 78.12 %, 79.86 %
    		* Best performance
    * Multi-channel with Deep CNN
    	* 8 subjects
    	* 64-channel, 1000 Hz -> 200 Hz
    	* Select 9 electrodes
    	* 1st baseline
    		* Feature extractor: FBCSP
    		* Feature selector: MIBIF
    		* classifier: NBPW
    		* 10-fold
    	* 2nd baseline
    		* Feature extractor: shallow CNN
    	* Deep CNN
    	* Deep CNN outperforms all methods (79.1 %)

## Discussion

    * Efficiency of the CNNs to learn features from raw EEG data
    * Robust end-to-end CNNs about transferring the knowledge inter-subjects
    * Interpretation about trained neural architecture using a back-propagation-based method and GAN

## Limitations

    * 2nd Baseline으로 Chebyshev type 2를 쓴 이유 -> 대체적으로 type I를 씀
    * 멀티 채널결과가 더 낮음 or 직접적인 비교가 안됨
    * subject adaptation의 문제
    * Hyperparameter 튜닝 문제
    * 베타밴드와 세타 밴드에서 유의한 차이를 시각적으로 확인하였으면 input representation에 따라 통계적으로 유의미한 결과를 확인했어야 하는것이 아닌가?
    * zero-training vs subject-independent
    * 6-norm을 사용한이유?
