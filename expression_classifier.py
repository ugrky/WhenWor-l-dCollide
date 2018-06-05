########## 1) IMPORT MAIN MODULES REQUIRED ##########
# To manipulate JSON into binary data:
import json 
# OpenCV Computer Vision Library
import cv2
# Required for multidimensional array operations
import numpy as np
########## IMPORT MAIN MODULES REQUIRED ##########




########## 2) BUILD THE SOCKET OBJECT FOR NETWORK COMMUNICATION:  ##########
# We need socket library of python for building UDP connection:
import socket
# The IP address of the computer that VDMX works on. Please specifcy the ip of other machine here:
UDP_IP = "123.68.9.1"
# The app running on other computer is listening to the port below for incoming facial expression data:
UDP_PORT = 5550
# We are creating socket object to use in each loop to send the result of each loop:
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
##########  BUILDING THE SOCKET OBJECT FOR NETWORK COMMUNICATION:  ##########




########## 3) CREATE THE FACE DETECTION OBJECT  ##########
# Create a face detection object from CascadeClassifier using the model provided by OpenCV
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
########## CREATING THE FACE DETECTION OBJECT ##########




########## 4) CREATING THE EMOTION DETECTOR  ##########
# We use load_model() method of keras to build the neural network layers:
from keras.models import load_model
# We create the emotion_classifier object from the trained model with FER data using load_model method of keras:
emotion_classifier = load_model('FER-2013-trained.hdf5', compile=False)
##########  CREATING THE EMOTION DETECTOR  ##########




########## 4) START VIDEO CAPTURE ##########
cv2.namedWindow('window_frame') 
video_capture = cv2.VideoCapture(0)
########## START VIDEO CAPTURE ##########


# MAIN LOOP FOR FACIAL EXPRESSION CLASSIFICATION:
while True:

    ########## 5) CAPTURE THE A SINGLE FRAME ##########
    capture_BGR = video_capture.read()[1]
    capture_GRAY = cv2.cvtColor(capture_BGR, cv2.COLOR_BGR2GRAY)
    capture_RGB = cv2.cvtColor(capture_BGR, cv2.COLOR_BGR2RGB)
    ########## CAPTURE A SINGLE FRAME ##########



    ########## 6) DETECT FACES ##########
    # Detect faces from "capture_GRAY" captured in previous process using CascadeClassifier Object trained with frontalface recognition model:
    # At the end of this process, faces multidimensional array contains the data of detected faces:
    all_faces = face_detector.detectMultiScale(capture_GRAY, 1.3, 5)
    ########## DETECT FACES ##########




    # For each detected face, do the following process:
    # (The OpenCV can detect multiple faces at once. So the data of multiple faces will go through the same process in a single frame)
    for coordinates in all_faces:


        ########## 7) FINAL PROCESS FACE FOR DETECTION ##########
        # Return the coordinates of faces in the captured image:
        x, y, width, height = coordinates
        x_off, y_off = (20, 40)
        x1, x2, y1, y2 = (x - x_off, x + width + x_off, y - y_off, y + height + y_off)

        # Crop only the face from image:
        gray_face = capture_GRAY[y1:y2, x1:x2]
        try:
            # We need a reference size for cropping the captured images. We get this reference from the trained dataset:
            emotion_target_size = emotion_classifier.input_shape[1:3]
            # We resize the image to our reference, so the AI could compare the captured data with the reference:
            gray_face = cv2.resize(gray_face, (emotion_target_size))
        except:
            continue

        # Last optimizations:
        gray_face = gray_face.astype('float32')
        gray_face = gray_face / 255.0
        gray_face = gray_face - 0.5
        gray_face = gray_face * 2.0
        gray_face = np.expand_dims(gray_face, 0)
        gray_face = np.expand_dims(gray_face, -1)
        ########## FINAL PROCESS FACE FOR DETECTION ########## 




        ########## 8) FINAL PROCESS FACE FOR DETECTION ##########
        emotion_prediction = emotion_classifier.predict(gray_face)
        # In the end of this process, we have the emotion prediction for this loop in the emotion_prediction arrray!
        ########## FINAL PROCESS FACE FOR DETECTION ##########




        ########## 9) UPDATE EMOTIONS OBJECT AND PRINT THE RESULTS: ##########
        # We have created Emotions object and using it as a central point to put current emotion values:
        from Emotion import emotions
        # We are manipulating the emotions object with the new emotions values coming from AI estimation: 
        emotions.reassignAll(emotion_prediction.tolist()[0][0], 
                                emotion_prediction.tolist()[0][2], emotion_prediction.tolist()[0][3], 
                                emotion_prediction.tolist()[0][4], emotion_prediction.tolist()[0][5], 
                                emotion_prediction.tolist()[0][6])
        # We are printing the estimation results:
        print("Angry:", emotions.returnEmotionValue("angry"))
        print("Happy:", emotions.returnEmotionValue("happy"))
        print("Sad:", emotions.returnEmotionValue("sad"))
        print("Surprised:", emotions.returnEmotionValue("surprise"))
        print("Fear:", emotions.returnEmotionValue("fear"))
        print("Neutral:", emotions.returnEmotionValue("neutral"))
        print(" ")
        print(" ")
        ########## UPDATE EMOTIONS OBJECT AND PRINT THE RESULTS: ##########




        ########## 10) NETWORK THE DATA: ##########
        # We are using the socket object created above to send the data to VDMX:
        sock.sendto(bytes(json.dumps(emotions.returnAll()), "utf-8"), (UDP_IP, UDP_PORT))
        ########## NETWORK: ##########



        # The rest of the code is not important for functionality
        # It is for displaying the result on the captured image:
        emotion_probability = np.max(emotion_prediction)
        emotion_labels = {0:'angry',1:'disgust',2:'fear',3:'happy', 4:'sad',5:'surprise',6:'neutral'}        
        emotion_label_arg = np.argmax(emotion_prediction)
        emotion_text = emotion_labels[emotion_label_arg]
        emotion_window = []
        emotion_window.append(emotion_text)

        if len(emotion_window) > 20:
            emotion_window.pop(0)
        try:
            from statistics import mode
            emotion_mode = mode(emotion_window)
        except:
            continue

        # Determine the color of the box on the camera capture:
        if emotion_text == 'angry':
            color = emotion_probability * np.asarray((255, 0, 0))
        elif emotion_text == 'sad':
            color = emotion_probability * np.asarray((0, 0, 255))
        elif emotion_text == 'happy':
            color = emotion_probability * np.asarray((255, 255, 0))
        elif emotion_text == 'surprise':
            color = emotion_probability * np.asarray((0, 255, 255))
        else:
            color = emotion_probability * np.asarray((0, 255, 0))
            
        color = color.astype(int)
        color = color.tolist()

        # Box for delimiting the face:
        x, y, w, h = coordinates
        cv2.rectangle(capture_RGB, (x, y), (x + w, y + h), color, 2)

        # The box writing the text:
        x, y = coordinates[:2]
        cv2.putText(capture_RGB, emotion_mode, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 1, cv2.LINE_AA)

    capture_BGR = cv2.cvtColor(capture_RGB, cv2.COLOR_RGB2BGR)
    cv2.imshow('window_frame', capture_BGR)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
