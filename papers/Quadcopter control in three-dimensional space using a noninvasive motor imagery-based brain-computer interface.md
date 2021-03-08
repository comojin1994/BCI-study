# Quadcopter control in three-dimensional space using a noninvasive motor imagery-based brain-computer interface

1. Conference or journal : Neural Engineering
2. Year : 2013
3. 1st author : Karl LaFleur
4. Professor : Bin He

## Goal

- BCI controlling a robotic quadcopter in 3D physical space using EEG

## Contribution

- First time the ability to control a drone in 3D physical space using EEG
- Suggest modified ITR metrics suitable for asynchronous, 2D BCI
  - Method of using at fixed schedule of events

## Method

1. Study overview
   - training and calibration phase, experimental task/control phase
2. Experimental subjects
   - 5 human subjects
3. Subject training
   - The reductionist control strategy
     - 1D(left, right) -> 1D(up, down) -> 2D -> Virtual Helicopter -> AR Drone(virtual) -> AR Drone(Real)
     - up: both hand squeezing or curling
4. Data collection and processing
   - 64-channel EEG
   - Using BCI2000’s online Autoregressive Filter
     - Using time sequential feature of data
     - EEGNet use data as image
5. Control environment and quadcopter
   - subjects did not directly see the quadcopter
   - Get feedback from camera mounted on the hull of the quadcopter

# Experiment

1. Experimental paradigm
   - 3 sessions per subject / 6~15 trials per session / 4 min per trial
   - Subjects were allowed to pass through the rings in any order
   - The signal used a threshold to remove minor signals
     - It used for remote control vehicles
   - Target hit, ring collision, wall collision
2. Experimental control
   - 3 subject controlled the flight of the quadcopter using keyboard
     - comparison between a standardized method of control and BCI control
   - To evaluate the intrinsic ease of the presented experimental task, a naive subject was shown a sham video feed of the helicopter
     - the performance of the AR Drone in the absence of user intent was measured
3. Performance analysis
   - ITR cannot be directly applied to asynchronous or pointing device BCIs
     - An unfixed schedule of commands would allow users to choose and perform activities as they would in a realistic manner
   - Modified ITR using Fitt’s law
   - Evaluate
     1. Speed of performance
        - average rings per maximum flight (ARMF)
        - average ring acquisition time (ARAT)
     2. Continuity of control
        - average crashes per maximum flight (ACMF)
     3. Success rate
        - percent total correct (PTC)
        - percent valid correct (PVC)
        - percent partial correct (PPC)

## Result

![](%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-03-07%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%208.44.17.png)
![](%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-03-07%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%208.44.36.png)

|Paradigm|Average ITR|
|_-_|_-_|
| keyboard |0.5 min|
|S1|1.74 min|
|S2|2.35 min|
|S3|2.5 min|
|S4|4.29 min|
|S5|2.1 min|
|avg|2.8 min|

![](%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-03-07%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%208.44.50.png)
![](%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-03-07%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%208.45.07.png)
![](%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-03-07%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%208.45.16.png)

## Discussion

    * real world에서의 문제들은 이전 연구에서는 다뤄지지 않았다.
    * Important difference in using the AR Drone quadcopter was the obligatory first-person perspective imposed on the subjects during real-world control
    * Learning the intrinsic unforeseen obstacles will allow for the creation of more realistic virtual simulations
    * Introduce an ITR metric applied to real world
    * Constant forward velocity and subject point of view improve performance
    * Subject engagement will increase when stimulated with a compelling virtual environment
    * This study purposely chose to focus on a telepresence implementation of drone control
    * By a balance of positive and negative motivators, subjects were compelled to higher levels of performance

## Limitation, Opinion

    * 당연한 이야기를 너무 많이 쓴것 같다
    	* ex. 방향을 틀면 속도가 준다,
    * Method 적으로 특별함이 없다
    * 좌,우 손 양손 등은 너무 잘 구분되는 특징인데 당연히 잘될수 밖에 없을것 같다
    * 수정된 ITR이 수식적으로 크게 어렵지 않은데 컨트리뷰션이라고 할수 있는지 모르겠다
    * 나이브 서브젝트에 대한 이해 부족 -> 정확히 어떻게 피드백을 받으면서 진행한 것인지
    * 원격으로 조절한다는것에 힘을 많이 준것같은 느낌인데 그것에 관한 이야기가 많지않다
    	* 통신문제가 발생한다는것을 돌려서 오히려 좋았다 라고 말하는 등
