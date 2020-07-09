from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import cv2
import os
import time
import os, re, os.path
import requests
import datetime
import keyboard
import pickle
import tkinter
from notify_run import Notify
import sys
from tkinter import messagebox
import PIL.Image, PIL.ImageTk
from functools import partial
import mail
global tkWindow
msk_bl=True
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
prototxtPath = os.path.sep.join(["face_detector", "deploy.prototxt"])
weightsPath = os.path.sep.join(["face_detector","res10_300x300_ssd_iter_140000.caffemodel"])
net = cv2.dnn.readNet(prototxtPath, weightsPath)
model = load_model("mask_detector.model")
faces=[]
def login():
    def validateLogin(username, password):
        un=username.get()
        ps=password.get()
        if un == "user" and ps == "pass":
            tkWindow.destroy()
            
        else:
            messagebox.showerror("Error", "Wrong Username or Password!")
         
    def disable_event():
        sys.exit()
        
    tkWindow = tkinter.Tk()  
    tkWindow.geometry('400x400')  
    tkWindow.title('Login')
    usernameLabel = tkinter.Label(tkWindow, text="User Name")
    usernameLabel.place(relx=0.15,rely=0.33,anchor=tkinter.CENTER)
    username = tkinter.StringVar()
    usernameEntry = tkinter.Entry(tkWindow, textvariable=username)
    usernameEntry.place(relx=0.55,rely=0.33,anchor=tkinter.CENTER)
    passwordLabel = tkinter.Label(tkWindow,text="Password")
    passwordLabel.place(relx=0.15,rely=0.66,anchor=tkinter.CENTER) 
    password = tkinter.StringVar()
    passwordEntry = tkinter.Entry(tkWindow, textvariable=password, show='*')
    passwordEntry.place(relx=0.55,rely=0.66,anchor=tkinter.CENTER)  
    validateLogin = partial(validateLogin, username, password)
    loginButton = tkinter.Button(tkWindow, text="Login", command=validateLogin)
    loginButton.place(relx=0.5,rely=0.8,anchor=tkinter.CENTER)  
    tkWindow.protocol("WM_DELETE_WINDOW", disable_event)
    tkWindow.mainloop()

def cap_detect():
    img_resp=requests.get('http://192.168.0.120:8080/shot.jpg')
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    img_arr=np.array(bytearray(img_resp.content),dtype=np.uint8)
    image=cv2.imdecode(img_arr,-1)
    #image=cv2.imread("C:\\ML\\face_mask\\examples\\example_03.png")
    (h, w) = image.shape[:2]
    blob = cv2.dnn.blobFromImage(image, 1.0, (300, 300),(104.0, 177.0, 123.0))
    face_arr=[]
    net.setInput(blob)
    detections = net.forward()
    
   
    for i in range(0, detections.shape[2]):
        
            confidence = detections[0, 0, i, 2]

            if confidence > 0.6:
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")

                (startX, startY) = (max(0, startX), max(0, startY))
                (endX, endY) = (min(w - 1, endX), min(h - 1, endY))
                
                face = image[startY:endY, startX:endX]
                orig =face
                face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
                face = cv2.resize(face, (224, 224))
                face = img_to_array(face)
                face = preprocess_input(face)
                face = np.expand_dims(face, axis=0)
                (mask, withoutMask) = model.predict(face)[0]
                #cv2.imwrite("C:\\ML\\face_mask\\op\\image.jpg",image)
                label = "Mask" if mask > withoutMask else "No Mask"
                fin="Mask" if mask > withoutMask else "No Mask"
                
                color = (0, 255, 0) if label == "Mask" else (0, 0, 255)
                faces.append([orig,label,now,image,fin])
                face_arr.append([orig,label,now,image,fin])
                label = "{}: {:.2f}%".format(label, max(mask, withoutMask) * 100)
                cv2.putText(image, label, (startX, startY - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
                cv2.rectangle(image, (startX, startY), (endX, endY), color, 2)
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                image=cv2.resize(image,(640,480))
                cv2.imwrite("C:\\ML\\face_mask\\op\\image.jpg",image) 
                
                """
                window = tkinter.Toplevel(win)
                window.title("Frame Evaluated")
                height, width, no_channels = image.shape
                canvas = tkinter.Canvas(window, width = width, height = height)
                canvas.pack()
                photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(image))
                 
                 
                canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)
                 
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                image=cv2.resize(image,(640,480))
                cv2.imwrite("C:\\ML\\face_mask\\op\\image.jpg",image) 
                #MAIL FOR SCRIPT

                
                window.mainloop()
                """
                #notify = Notify()
                
                """
                if fin=='Mask':
                    #mail.mask()
                    #messagebox.showinfo(title="Safe", message="Mask detected! Mail Sent!")
                    print("mask")
             
                    
                    notify.send('SAFE!!')
                    print('sent')
                else:
                    #mail.no_mask()
                    #msk_bl=False
                    #messagebox.showinfo(title="Unsafe", message="Mask Not Detected! Mail Sent!")
                    #return
                    print("NO MASK")
                    
                    
                    notify.send('UNSAFE!!')
                    print("SENT")
                    
                mypath ='C:\\ML\\face_mask\\op'
                for root, dirs, files in os.walk(mypath):
                    for file in files:
                        os.remove(os.path.join(root, file))
                return
                """
                
                """
            else:
                messagebox.showerror("Error", "No Faces Detected! Try Again")
                return
                """
    if(len(face_arr))==0:
        messagebox.showerror("Error", "No Faces Detected! Try Again")
        return
    else:
        #print(len(face_arr))
        for i in range(0,len(face_arr)):
            #print(face_arr[i][4])
            if face_arr[i][4]=="No Mask":
                messagebox.showinfo(title="Unsafe", message="Mask Not Detected! Mail Sent!")
                #mail.no_mask()
                return
        messagebox.showinfo(title="Safe", message="Mask detected! Mail Sent!")
        return
        
                
        
            
    

def save():
    with open('faces.pkl', 'wb') as f:
            pickle.dump(faces, f)
            
def show_frame():
    mainWindow = tkinter.Toplevel(win)
    mainWindow.geometry('760x520')
    win.configure(background = "white")
    mainWindow.resizable(0,0)
    # mainWindow.overrideredirect(1)

    mainFrame = tkinter.Frame(mainWindow)
    mainFrame.place(x=20, y=20)                

    #Capture video frames
    lmain = tkinter.Label(mainFrame)
    lmain.grid(row=0, column=0)

    cap = cv2.VideoCapture('http://192.168.0.120:8080/video')

    def show_frame():
        ret, frame = cap.read()

        cv2image   = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

        img   = PIL.Image.fromarray(cv2image).resize((720,480))
        imgtk = PIL.ImageTk.PhotoImage(image = img)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        lmain.after(10, show_frame)

    closeButton = tkinter.Button(mainWindow, text = "CLOSE",width = 20, height= 1)
    closeButton.configure(command= lambda: mainWindow.destroy())              
    closeButton.place(x=270,y=430)	

    show_frame()  #Display
    mainWindow.mainloop() 
    
    

login()         
win = tkinter.Tk()
win.title("Mask Detection")
win.geometry('500x500')
win.configure(background = "white")
lb=tkinter.Label(win,text="Mask Detection",font=("Helvetica", 16),width=50,height=1)
lb.place(relx=0.5,rely=0.0,anchor=tkinter.N)
button=tkinter.Button(win, text="START DETECTION",command=cap_detect)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
button1=tkinter.Button(win, text="SAVE",command=save)
button1.place(relx=0.5, rely=0.25, anchor=tkinter.CENTER)
button2=tkinter.Button(win, text="WATCH LIVE FOOTAGE",command=show_frame)
button2.place(relx=0.5, rely=0.75, anchor=tkinter.CENTER)
win.mainloop()
    


        

        
        

        
