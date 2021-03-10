# Quadcopter flight control using a low-cost hybrid interface with EEG-based classification and eye tracking

1. Conference or journal (IF): Computers in Biology and Medicine (Comput. Biol. Med.) (Q3)
2. Year : 2014
3. 1st author :Byung Hyung Kim
4. Professor : Sungho Jo (KAIST 전산학부)

## Goal

    * The suggestion of a low-cost hybrid EEG based BCI system to control the quadcopter in 3-D space

## Contribution

    * Easy-to-learn and easy-to-use system
    * Not only low-cost bust also a convenient wearable device

## Method

    * Use of a cost-effective eye tracker and an EEG device
    * Eye tracker
    	* Image processing acquired from the eye tracker
    		* Image binarization
    		* Eye features extraction
    		* Outlier removal through RANSAC
    	* Interpolation of gaze points using a 2nd-order polynomial
    [image:26D5AAF3-308E-4025-A069-90FA9E8169AC-1798-0000155DE87829D7/스크린샷 2021-03-09 오후 3.44.28.png]
    	* Obtaining coefficients using a least-squares method
    * EEG device
    	* Feature extraction using CSP, AR
    	* Classification using SVM
    	* Use of time window for robust classification performance
    * Control of the quadcopter with the 8 directions
    * Use of 2 kinds of GUI window for selection
    	*

## Experiment

    * EEG data acquisition
    	* 8 s. for each trial
    		* 1st 4 s.: non-concentrated state (alpha wave, 11 ~ 13 Hz)
    		* Next 4 s.: concentration state (beta wave, 13 ~ 19 Hz)
    	* Usage of statistical method to overcome inter- and intra-subject variability issue
    * EOG data acquisition
    	* 1 min. per point
    * Two-step experiment
    	* The keyboard-based interface system
    	* The hybrid component
    	* Drone control along a defined path
    * Evaluation of performance
    	* Travelled distance (TD)
    	* Total time taken (TT)
    	* Normalized path length (NPL)
    	* Area Under the Curve (AUC)
    	* Speed of control
    	* Success rate (SR)

## Result

    * Achievement of the enough AUC score to judge as efficient
    * Achievement of the 85.55% SR score compared to the keyboard-based system
    * Sufficient performance of the BCI-based hybrid service for real-time service

## Discussion

    * Competitive performances of the hybrid interface compared to the keyboard-based system
    * The issue about artifacts in EEG data from eye movements
    	* Incomplete noise removal algorithm
    * Differentiated advantage of eye tracking-based system
    * Inconsistent EEG pattern problem due to fatigue and anxiety

## Limitation, opinion

    * 방향이동이 직관적이지 않다
    * AUC를 계산할 때 정답에 대한 정의가 분명하지 않다
    	* 가상환경에서의 실험도 BCI로 했으면 정확도가 높을 수 밖에 없을것 같음
    * 눈이 깜빡일때도 상상에 대한 데이터가 포함되어 있을텐데 ICA를 사용하여도 데이터 손실이 있지 않을까
    * 긴장도에 따라 피험자의 안구의 움직임이 불안정해 질 수 있음
