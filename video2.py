from imutils.video import FPS
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from imutils.video import VideoStream
import numpy as np
import argparse
import imutils
import time
import cv2
import pickle
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

print("[INFO] loading model...")
net = cv2.dnn.readNetFromCaffe("C:\\ML\\face_mask\\detect_faces\\face_detector\\deploy.prototxt","C:\\ML\\face_mask\\detect_faces\\face_detector\\res10_300x300_ssd_iter_140000.caffemodel")
maskNet = load_model("mask_detector.model")
#vs = VideoStream(src="D:\\Old Laptop\\Mukund Files 21-04-19\\MUKUND\\ENTERTAINMENT\\ds.mp4").start()
#vs = VideoStream(src=0).start()
#vs=cv2.VideoCapture("C:\\Users\\Mukund\\Downloads\\test.mp4")
vs=cv2.VideoCapture("http://192.168.0.104:8080/video")
#vs=cv2.VideoCapture(0)
faces=[]
face_last=[]
ct=0
fps = FPS().start()
while True:
    ct+=1 
    time.sleep(1)
    #frame = vs.read()
    ret,frame=vs.read()
    #frame = imutils.resize(image, width=1000)
    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0,
        (300, 300), (104.0, 177.0, 123.0))
    net.setInput(blob)
    detections = net.forward()
    for i in range(0, detections.shape[2]):
        
        confidence = detections[0, 0, i, 2]

        if confidence < 0.6:
            continue
        
        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")
        
        (startX, startY) = (max(0, startX), max(0, startY))
        (endX, endY) = (min(w - 1, endX), min(h - 1, endY))
        roi_color=frame[startY:endY,startX:endX]
        facel=[]
        if ct==3:
            face_last.append([frame,roi_color])
            faces.append(roi_color)
            facel.append(roi_color)
            for face in facel:
                face = frame[startY:endY, startX:endX]
                face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
                face = cv2.resize(face, (224, 224))
                face = img_to_array(face)
                face = preprocess_input(face)
                face = np.expand_dims(face, axis=0)
                preds = maskNet.predict(face)
                print(len(preds))
                for pred in preds:
                    if pred[0] > pred[1]:
                        print("mask")
                    else:
                        print("No mask")
            
        #text = "{:.2f}%".format(confidence * 100)
        y = startY - 10 if startY - 10 > 10 else startY + 10
        cv2.rectangle(frame, (startX, startY), (endX, endY),(0, 0, 255), 2)
        #cv2.putText(frame, text, (startX, y),cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
         

    fps.update()
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF


    if key == ord("q") or ct==4:
        break


fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

cv2.destroyAllWindows()
vs.release()  
temp=len(faces)
print(len(faces))
with open('faces.pkl', 'wb') as f:
    pickle.dump(face_last, f)