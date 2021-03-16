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

## Discussion

## Limitations

    * 여러 CNN branch를 구성함으로 계산의 비효율성 증가
    * subject의 수와 정확도의 상관관계가 없음
