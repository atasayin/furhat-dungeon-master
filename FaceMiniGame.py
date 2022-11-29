# -*- coding: utf-8 -*-
import cv2
from deepface import DeepFace
import numpy as np
import matplotlib.pyplot as plt
import keyboard
import time


def new():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        cap = cv2.VideoCapture(1)
    if not cap.isOpened():
        raise IOError("CANNOT OPEN WEBCAM")

    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
    while True:
        ret,frame =cap.read()
        plt.imshow(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB))
        result = DeepFace.analyze(frame,actions = ['emotion'])

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray,1.1,4)
        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,2255,0),2)
        font = cv2.FONT_HERSHEY_SIMPLEX

        cv2.putText(frame,result['dominant_emotion'], (50,50),font,3,(0,0,255),2,cv2.LINE_4)
        cv2.imshow('Original video',frame)
        key=cv2.waitKey(1) 
        if key==ord('q'):   # here we are specifying the key which will stop the loop and stop all the processes going
            break
    cap.release()
    cv2.destroyAllWindows()

        
def preap_model():
    face_cascade_name = cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml'  #getting a haarcascade xml file
    face_cascade = cv2.CascadeClassifier()  #processing it for our project
    if not face_cascade.load(cv2.samples.findFile(face_cascade_name)):  #adding a fallback event
        print("Error loading xml file")
    return face_cascade

def capture_face(face_cascade):
    video=cv2.VideoCapture(0)
    while video.isOpened():  #checking if are getting video feed and using it
            _,frame = video.read()

            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  #changing the video to grayscale to make the face analisis work properly
            face=face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)

            for x,y,w,h in face:
                img=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),1)  #making a recentangle to show up and detect the face and setting it position and colour

            #making a try and except condition in case of any errors
                try:
                    analyze = DeepFace.analyze(frame,actions=['emotions'])  #same thing is happing here as the previous example, we are using the analyze class from deepface and using ‘frame’ as input
                    print(analyze['dominant_emotion'])  #here we will only go print out the dominant emotion also explained in the previous example
                except:
                    print("no face")

            #this is the part where we display the output to the user
            cv2.imshow('video', frame)
            key=cv2.waitKey(1) 
            if key==ord('q'):   # here we are specifying the key which will stop the loop and stop all the processes going
                break
    video.release()



def capture_write(filename="image.jpeg", port=0, ramp_frames=30, x=1280, y=720):
    camera = cv2.VideoCapture(port)

    # Set Resolution
    camera.set(3, x)
    camera.set(4, y)

    # Adjust camera lighting
    for i in range(ramp_frames):
        temp = camera.read()
    retval, im = camera.read()
    cv2.imwrite(filename,im)
    del(camera)
    return True

def check_emotion(obj,emotion_list,turn,life):
    turn = turn-1
    emotion = emotion_list[turn]
    print(emotion)
    #define percantage range to be considered as matching print emotion statmnet should be changed look at keyboard waiting things

    if obj.get(emotion[1]) == emotion[2]:
                print(f" YOU MATCHED {emotion[1]} WITH {emotion[1+1]} percent")
    else:
                print(f" YOU DID NOT MATCHED YOUR EMOTIONS WERE : {obj}")
                life = life - 1
                print(f" YOU LOST A LIFE :( REAMINING LIFE COUNT: {life}")
                
    return life


def main():
    l1= ((('Fear 80% and Sad 10%'),'fear',80,'sad',10), (('Angry 70% Disgust 10%'),'angry',70,'disgut',10),(('Happy 80%'),'happy',80))
    print("hello")
    life_count =3
    for i in range(1,4):
        print(f"NOW YOU ARE IN TURN {i} ")
        print(f"IN TURN {i} YOU NEED TO MATCH {l1[i-1][0]} percentages ")
        print("Press q to continue...")
        #keyboard.wait("esc")
        # while True:
        #     if keyboard.is_pressed("q"): #returns True if "q" is pressed
        #         print("You pressed q")
        #         break #break the while loop is "q" is pressed
        time.sleep(5)
        capture = capture_write()
        if capture:
            obj = DeepFace.analyze(img_path = "image.jpeg", 
                actions = ['age', 'gender', 'race', 'emotion'])
        print(obj.get('emotion'))
        life_count = check_emotion(obj,l1,i,life_count)
        print("Press q to continue...")
        #keyboard.wait("esc")
        #while True:
        #    if keyboard.is_pressed("q"): #returns True if "q" is pressed
        #        print("You pressed q")
        #        break #break the while loop is "q" is pressed
        time.sleep(5)
    #models = ['VGG-Face', 'Facenet', 'OpenFace', 'DeepFace', 'DeepID', 'Dlib']
    #result = DeepFace.stream(db_path = "C:/facial_db", model_name = models[1])
    #print(result)
    #face_cascade = preap_model()
    #capture_face(face_cascade)





if __name__ == "__main__":
    main()