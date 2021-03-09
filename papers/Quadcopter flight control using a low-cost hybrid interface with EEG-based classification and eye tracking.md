# Quadcopter flight control using a low-cost hybrid interface with EEG-based classification and eye tracking

1. Conference or journal : Computer in Biology and Medicine (Comput. Biol. Med.)
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
    ![](%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-03-09%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%203.44.28.png)
    	* Obtaining coefficients using a least-squares method
    * EEG device
    	* Feature extraction using CSP, AR
    	* Classification using SVM
    	* Use of time window for robust classification performance
    * Control of the quadcopter with the 8 directions

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
    	*

## Result

## Discussion

## Limitation, opinion

    * 방향이동이 직관적이지 않다
