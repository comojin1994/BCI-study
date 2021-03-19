# Subject-Independent Brain–Computer Interfaces Based on Deep Convolutional Neural Networks

1. Conference or journal (Quartile): IEEE Transactions on Neural Networks and Learning Systems (IEEE Trans. Neural Netw. Learn. Syst) (Q1, 3%)
2. Year : 2020
3. 1st author : O-Yeon Kwon
4. Professor : Seong-Whan Lee
5. Univ.: Korea Univ.

## Goal

    * Suggestion of a novel framework of spectral-spatial feature representation using CNNs from a large-scale MI EEG database

## Contributions

    * Construction of the largest MI-based database
    * Suggestion of a new discriminative spectral-spatial input
    * Representation of the MI-induced ERD pattern through the CNN model

## Methods

    * Related works
    	* CSSP, FBCSP, BSSFO methods require the calibration procedure to train the decoder
    	* 2 key issues
    		1. No large-scale MI database with a large number of subjects and sessions
    		2. Scarce studies on subject-independent BCIs-based on DL
    * Data acquisition and experimental setup
    	* 54 healthy subjects
    	* the interval between the sessions was between one and two weeks
    	* Downsampled to 100 Hz by the Nyquist theory
    	* MI paradigm
    		* 3 s with fixation cross
    		* 4 s for performing the MI task
    		* 6 s for rest
    		* experiment is composed of an offline and an online phase
    * Spectral-Spatial Feature Representation (SSFR)
    	* Spectral-Spatial Input generation
    		* bandpass-filtered with 5-order Butterworth filter (Use of bands in reference to. previous findings)
    		* Usage of CSP
    		* Get variance of the spatially filtered signal and re-ordered the band by using mutual information
    		* Select top 20 csp filters based on re-ordered band
    		* get covariance matrix
    	* Feature Representation Using CNN
    		* Construct CNN model to learn representation from a set of spectral-spatial inputs
    	* Feature fusion and classification
    		* integration of all the segments data that contain the discriminant ERD patterns in the brain signals
    	* Performance evaluation
    		* subject-independent: fused model, MR FBCSP, pooled CSP
    		* subject-dependent: CSP, CSSP, FBCSP, BSSFO
    		* classifier: LDA
    		* Train-test-split
    			* subject-independent: leave-one-subject-out cross-validation
    			* subject-dependent: session2 1st-offline training, session2 2nd-online testing

[image:31C0C790-3362-4BE3-9A89-4924F7AF18C1-816-0000177048A41D65/스크린샷 2021-03-15 오후 4.19.09.png]

## Experiments

## Results

    * subject-independent: 74.15% (acc)
    * subject-dependent: 71.02% (acc)
    * kernel size: 3x3, # of feature map: 10, 14,18
    * No relation with # of subjects
    * Positive relation with # of frequency band

## Discussion

    * statistical hypothesis test to prove the efficiency of the model
    * Model performance according to the number of subjects and frequency band
    * Suggestion of new input feature based-on CSP
    * Suggestion of model which trained all frequency bands individually with concatenation fusion technique
    * Suggestion of frequency-wise operation model & feature fusion model
    * Subject independent model balance between excellent and poor subjects
    * more subjects less variation, more frequency higher performance

## Limitations

    * 여러 CNN branch를 구성함으로 계산의 비효율성 증가
    * subject의 수와 정확도의 상관관계가 없음
    * subject dependent method가 independent보다 정확도가 낮음
    	* subject independent에서 잘 동작 하려면 데이터의 feature를 잘 뽑아야하기 때문에 subject dependent에서도 잘 동작해야할 것 같음
    * frequency 개수에 따른 결과 분석 그래프 이상함
    * Use of other types of inputs
    * Necessity about more informative visualization tool
    * Use of pertained model
    * frequency 별 정확도에서 최고치랑 classification 정확도랑 다름
    * (추가)여러 채널을 사용하는것으로 인해 발생하는 상용화 문제
