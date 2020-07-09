# Face-Mask-Detection-System
This program, which is connected to a webcam situated on the door, captures the video, detects faces and checks whether the faces have a mask on. The software also consists of a Graphical User Interface (GUI), which notifies users inside the house about the detections and sends appropriate messages. 
Uses OpenCV, Keras and Deep Learning. 
Deployed this software in my apartment for real time testing.
## Working of the program with screenshots
### 1.Login Page

![Login Page](https://github.com/mukundacharya/Face-Mask-Detection-System/blob/master/examples/login.png?raw=true)
### 2.Home Page
There are options to save the faces, start detection and watch the live footage captured from the webcam.

![Home Page](https://github.com/mukundacharya/Face-Mask-Detection-System/blob/master/examples/homepage.png?raw=true)
### 3.Detection of Faces.
If the user clicks the "START DETECTION" Button, the programs captures a frame from the webcam, runs the mask detection algorithm, all in the background, and determines the user whether the visitors are safe to enter or not.

If all the guests are wearing a mask, the program signifies in the screen that masks are detected and also sends an e-mail with the image captured that the person(s) is/are safe.

![Mask detected](https://github.com/mukundacharya/Face-Mask-Detection-System/blob/master/examples/mask_detected.png?raw=true) 

The email screenshot is-

![Mask detected mail](https://github.com/mukundacharya/Face-Mask-Detection-System/blob/master/examples/mask_mail.png?raw=true)

Same is the case for faces detected with no mask.

![Mask detected](https://github.com/mukundacharya/Face-Mask-Detection-System/blob/master/examples/nask_not_detected.png?raw=true) 

The email screenshot is-

![Mask detected mail](https://github.com/mukundacharya/Face-Mask-Detection-System/blob/master/examples/no_mask_mail.png?raw=true)

### 4.If No faces are detected, the user is alterted.

![Mask detected mail](https://github.com/mukundacharya/Face-Mask-Detection-System/blob/master/examples/no_face_detected.png?raw=true)

### 5. Video Surveillance
Users can watch live video from the webcam.

![Mask detected mail](https://github.com/mukundacharya/Face-Mask-Detection-System/blob/master/examples/live_footage.png?raw=true)

To execute the program, run the photo.py file.
