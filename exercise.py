#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import mediapipe as mp
import numpy as np
import pyttsx3
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from tkinter import messagebox
from PIL import ImageTk, Image
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import pickle
import os


# In[2]:


# Initialize pyttsx3 engine
engine = pyttsx3.init()
model_path = r'F:\RealTimeFitnessTrainer\humanmodel.pickel'


# In[3]:


# Check if the model file exists
if not os.path.exists(model_path):
    print(f"Error: The file {model_path} does not exist.")
else:
    # Load the model
    pickle_in = open(model_path, "rb")
    model = pickle.load(pickle_in)


# In[4]:


mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose


# In[5]:


def calculate_angle(a, b, c):
    a = np.array(a)  # First point
    b = np.array(b)  # Mid point
    c = np.array(c)  # End point
    
    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)
    
    if angle > 180.0:
        angle = 360 - angle
        
    return angle


# In[6]:


def say(command):
    print(f"Saying: {command}")  # Debug statement
    
    engine.say(command)
    engine.runAndWait()


# In[7]:


# Test the say function
say("Testing audio output")


# In[25]:


# def jumping_jack(x):
#     say("Starting the Jumping Jack exercise. Please stand in front of the camera.")
    
#     cap = cv2.VideoCapture(0)
#     cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # Set lower resolution
#     cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
#     count = 0 
#     flag = 0  # Initialize flag for counting jumps
#     exercise_complete = False  # Flag to indicate if the exercise is complete

#     with mp_pose.Pose(min_detection_confidence=0.3, min_tracking_confidence=0.3) as pose:  # Lower confidence threshold for better performance
#         while cap.isOpened():
#             if exercise_complete:
#                 break

#             ret, frame = cap.read()

#             image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#             image.flags.writeable = False
#             results = pose.process(image)
#             image.flags.writeable = True
#             image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

#             try:
#                 landmarks = results.pose_landmarks.landmark
                
#                 a = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
#                 b = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
#                 c = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x, landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]

#                 angle = calculate_angle(a, b, c)

#                 if angle < 87:  # Adjusted lower threshold
#                     if flag == 0:
#                         say("Jump up")
#                     flag = 1
#                 if angle > 104 and flag == 1:  # Adjusted upper threshold
#                     flag = 0
#                     count += 1
#                     say(f"Jumping Jack Count: {count}")

#             except Exception as e:
#                 print(f"Error processing frame: {e}")

#             # Display instructions and count on the screen
#             cv2.putText(image, 'Jumping Jack Exercise', (15, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
#             cv2.putText(image, 'Count', (15, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
#             cv2.putText(image, str(count), (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

#             # Draw landmarks and connections
#             mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

#             cv2.imshow('Jumping Jack', image)

#             if cv2.waitKey(10) & 0xFF == ord('q'):
#                 break
#             if count >= x:
#                 say("Jumping Jack exercise complete")
#                 exercise_complete = True  # Set the flag to true to stop the exercise
#                 break

#         cap.release()
#         cv2.destroyAllWindows()


# In[9]:


def right_leg_rise(x):
    say("Starting the Right Leg Rise exercise. Please stand in front of the camera and lift your right leg.")
    
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # Set lower resolution
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    count = 0 
    flag = 0  # Initialize flag for counting leg lifts
    exercise_complete = False  # Flag to indicate if the exercise is complete

    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            if exercise_complete:
                break

            ret, frame = cap.read()

            frame = cv2.flip(frame, 1)

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = pose.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            try:
                landmarks = results.pose_landmarks.landmark

                a = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
                b = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
                c = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x, landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]

                angle = calculate_angle(a, b, c)

                cv2.putText(image, f"Angle: {angle}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

                if angle < 100:
                    if flag == 0:
                        say("Lift your right leg higher")
                    flag = 1
                if angle > 120 and flag == 1:
                    flag = 0
                    count += 1
                    say(f"Right Leg Rise Count: {count}")

            except Exception as e:
                print(f"Error processing frame: {e}")

            # Display count on the screen
            cv2.putText(image, 'Right Leg Rise Exercise', (15, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
            cv2.putText(image, 'Count', (15, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(image, str(count), (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

            # Draw landmarks and connections
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            cv2.imshow('Right Leg Rise', image)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
            if count >= x:
                say("Right Leg Rise exercise complete")
                exercise_complete = True

        cap.release()
        cv2.destroyAllWindows()


# In[10]:


def left_leg_rise(x):
    say("Starting the left leg rise exercise. Please stand in front of the camera.")
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # Set lower resolution
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    count = 0 
    flag = 0

    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = pose.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            try:
                landmarks = results.pose_landmarks.landmark

                a = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
                b = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x, landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
                c = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]

                angle = calculate_angle(a, b, c)

                cv2.putText(image, f"Angle: {angle}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

                if angle < 100:
                    if flag == 0:
                        say("Lift your left leg")
                    flag = 1
                if angle > 120 and flag == 1:
                    flag = 0
                    count += 1
                    say(f"left Leg Rise Count: {count}")

            except Exception as e:
                print(f"Error processing frame: {e}")

            cv2.putText(image, 'left Leg Rise exercise', (15, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (40, 50, 155), 2, cv2.LINE_AA)
            cv2.putText(image, 'COUNT: '+str(count), (15, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (244, 110, 34), 2, cv2.LINE_AA)
            # cv2.putText(image, str(count), (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            cv2.imshow('left Leg Rise', image)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
            if count >= x:
                say("left Leg Rise exercise complete")
                break

        cap.release()
        cv2.destroyAllWindows()


# In[11]:


def squat(x):
    say("Starting the Squat exercise. Please stand in front of the camera.")
    
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    count = 0  
    flag = 0  
    exercise_complete = False  

    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            if exercise_complete:
                break

            ret, frame = cap.read()

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = pose.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            try:
                landmarks = results.pose_landmarks.landmark

                a = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x, landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
                b = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x, landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
                c = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]

                angle = calculate_angle(a, b, c)

                if angle < 87:
                    if flag == 0:
                        say("Squat Down")
                    flag = 1
                if angle > 104 and flag == 1:
                    flag = 0
                    count += 1
                    say(f"Squat Count: {count}")

            except Exception as e:
                print(f"Error processing frame: {e}")

            cv2.putText(image, 'Squat Exercise', (15, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
            cv2.putText(image, 'Count', (15, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(image, str(count), (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            cv2.imshow('Squat', image)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
            if count >= x:
                say("Squat exercise complete")
                exercise_complete = True

        cap.release()
        cv2.destroyAllWindows()


# In[12]:


def walking_jog(x):
    say("Starting the Walking Jogging exercise. Please stand in front of the camera.")
    
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    count = 0  
    flag = 0  
    exercise_complete = False  

    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            if exercise_complete:
                break

            ret, frame = cap.read()

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = pose.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            try:
                landmarks = results.pose_landmarks.landmark

                a = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                b = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                c = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]

                angle = calculate_angle(a, b, c)

                if angle < 87:
                    if flag == 0:
                        say("Walk Jog")
                    flag = 1
                if angle > 104 and flag == 1:
                    flag = 0
                    count += 1
                    say(f"Walk Jogging Count: {count}")

            except Exception as e:
                print(f"Error processing frame: {e}")

            cv2.putText(image, 'Walk Jogging Exercise', (15, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
            cv2.putText(image, 'Count', (15, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(image, str(count), (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            cv2.imshow('Walking Jogging', image)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
            if count >= x:
                say("Walking Jogging exercise complete")
                exercise_complete = True

        cap.release()
        cv2.destroyAllWindows()


# In[13]:


def biceps_curl(x):
    say("Starting the Biceps Curl exercise. Please stand in front of the camera and hold a weight in your hand.")
    
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    count = 0  
    flag = 0  
    exercise_complete = False  

    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            if exercise_complete:
                break

            ret, frame = cap.read()

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = pose.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            try:
                landmarks = results.pose_landmarks.landmark

                a = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                b = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
                c = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]

                angle = calculate_angle(a, b, c)

                if angle < 87:
                    if flag == 0:
                        say("Lift your weight towards your shoulder")
                    flag = 1
                if angle > 104 and flag == 1:
                    flag = 0
                    count += 1
                    say(f"Biceps Curl Count: {count}")

            except Exception as e:
                print(f"Error processing frame: {e}")

            cv2.putText(image, 'Biceps Curl Exercise', (15, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
            cv2.putText(image, 'Count', (15, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(image, str(count), (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            cv2.imshow('Biceps Curl', image)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
            if count >= x:
                say("Biceps Curl exercise complete")
                exercise_complete = True

        cap.release()
        cv2.destroyAllWindows()


# In[35]:


def jumping_jack(x):
    print("Starting the Jumping Jack exercise.")
    say("Starting the Jumping Jack exercise. Please stand in front of the camera.")
    
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Camera not accessible")
        return

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    print('Camera opened')
    
    count = 0  
    flag = 0  
    exercise_complete = False  

    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            if exercise_complete:
                break

            ret, frame = cap.read()
            if not ret:
                print("Error: Failed to capture frame")
                break

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = pose.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            try:
                landmarks = results.pose_landmarks.landmark
                print(f"Landmarks detected: {len(landmarks)}")

                a = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                b = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                c = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]

                angle = calculate_angle(a, b, c)

                if angle < 87:
                    if flag == 0:
                        say("Jumping Jack")
                    flag = 1
                if angle > 104 and flag == 1:
                    flag = 0
                    count += 1
                    say(f"Jumping Jack Count: {count}")

            except Exception as e:
                print(f"Error processing frame: {e}")

            cv2.putText(image, 'Jumping Jack Exercise', (15, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
            cv2.putText(image, 'Count', (15, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(image, str(count), (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            cv2.imshow('Jumping Jack', image)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
            if count >= x:
                say("Jumping Jack exercise complete")
                exercise_complete = True

        cap.release()
        cv2.destroyAllWindows()


# In[15]:


def lunge(x):
    say("Starting the Lunge exercise. Please stand in front of the camera.")
    
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    count = 0  
    flag = 0  
    exercise_complete = False  

    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            if exercise_complete:
                break

            ret, frame = cap.read()

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = pose.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            try:
                landmarks = results.pose_landmarks.landmark

                a = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x, landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
                b = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x, landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
                c = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]

                angle = calculate_angle(a, b, c)

                if angle < 87:
                    if flag == 0:
                        say("Lunge")
                    flag = 1
                if angle > 104 and flag == 1:
                    flag = 0
                    count += 1
                    say(f"Lunge Count: {count}")

            except Exception as e:
                print(f"Error processing frame: {e}")

            cv2.putText(image, 'Lunge Exercise', (15, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
            cv2.putText(image, 'Count', (15, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(image, str(count), (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            cv2.imshow('Lunge', image)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
            if count >= x:
                say("Lunge exercise complete")
                exercise_complete = True

        cap.release()
        cv2.destroyAllWindows()


# In[16]:


def plank(x):
    say("Starting the Plank exercise. Please stand in front of the camera.")
    
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    count = 0  
    flag = 0  
    exercise_complete = False  

    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            if exercise_complete:
                break

            ret, frame = cap.read()

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = pose.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            try:
                landmarks = results.pose_landmarks.landmark

                a = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                b = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                c = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

                angle = calculate_angle(a, b, c)

                if angle < 150:
                    if flag == 0:
                        say("Hold the Plank position")
                    flag = 1
                if angle > 170 and flag == 1:
                    flag = 0
                    count += 1
                    say(f"Plank Count: {count}")

            except Exception as e:
                print(f"Error processing frame: {e}")

            cv2.putText(image, 'Plank Exercise', (15, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
            cv2.putText(image, 'Count', (15, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(image, str(count), (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            cv2.imshow('Plank', image)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
            if count >= x:
                say("Plank exercise complete")
                exercise_complete = True

        cap.release()
        cv2.destroyAllWindows()


# In[17]:


def push_up(x):
    say("Starting the Push-Up exercise. Please stand in front of the camera.")
    
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    count = 0  
    flag = 0  
    exercise_complete = False  

    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            if exercise_complete:
                break

            ret, frame = cap.read()

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = pose.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            try:
                landmarks = results.pose_landmarks.landmark

                a = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                b = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                c = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

                angle = calculate_angle(a, b, c)

                if angle < 90:
                    if flag == 0:
                        say("Perform Push-Up")
                    flag = 1
                if angle > 150 and flag == 1:
                    flag = 0
                    count += 1
                    say(f"Push-Up Count: {count}")

            except Exception as e:
                print(f"Error processing frame: {e}")

            cv2.putText(image, 'Push-Up Exercise', (15, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
            cv2.putText(image, 'Count', (15, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(image, str(count), (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            cv2.imshow('Push-Up', image)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
            if count >= x:
                say("Push-Up exercise complete")
                exercise_complete = True

        cap.release()
        cv2.destroyAllWindows()


# In[18]:


def crunches(x):
    say("Starting the Crunches exercise. Please stand in front of the camera.")
    
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    count = 0  
    flag = 0  
    exercise_complete = False  

    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            if exercise_complete:
                break

            ret, frame = cap.read()

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = pose.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            try:
                landmarks = results.pose_landmarks.landmark

                a = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x, landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
                b = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                c = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]

                angle = calculate_angle(a, b, c)

                if angle < 110:
                    if flag == 0:
                        say("Perform Crunches")
                    flag = 1
                if angle > 130 and flag == 1:
                    flag = 0
                    count += 1
                    say(f"Crunches Count: {count}")

            except Exception as e:
                print(f"Error processing frame: {e}")

            cv2.putText(image, 'Crunches Exercise', (15, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
            cv2.putText(image, 'Count', (15, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(image, str(count), (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            cv2.imshow('Crunches', image)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
            if count >= x:
                say("Crunches exercise complete")
                exercise_complete = True

        cap.release()
        cv2.destroyAllWindows()


# In[19]:


def triceps_dip(x):
    say("Starting the Triceps Dip exercise. Please stand in front of the camera.")
    
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    count = 0  
    flag = 0  
    exercise_complete = False  

    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            if exercise_complete:
                break

            ret, frame = cap.read()

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = pose.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            try:
                landmarks = results.pose_landmarks.landmark

                a = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                b = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                c = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

                angle = calculate_angle(a, b, c)

                if angle < 90:
                    if flag == 0:
                        say("Perform Triceps Dip")
                    flag = 1
                if angle > 130 and flag == 1:
                    flag = 0
                    count += 1
                    say(f"Triceps Dip Count: {count}")

            except Exception as e:
                print(f"Error processing frame: {e}")

            cv2.putText(image, 'Triceps Dip Exercise', (15, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
            cv2.putText(image, 'Count', (15, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(image, str(count), (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            cv2.imshow('Triceps Dip', image)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
            if count >= x:
                say("Triceps Dip exercise complete")
                exercise_complete = True

        cap.release()
        cv2.destroyAllWindows()


# In[20]:


# Dictionary mapping exercise names to their respective functions
exercise_functions = {
    "Left Leg Rise": left_leg_rise,
    "Squat": squat,
    "Walking Jogging": walking_jog,
    "Biceps Curl": biceps_curl,
    "Jumping Jack": jumping_jack,
    "Lunge": lunge,
    "Plank": plank,
    "Push-Up": push_up,
    "Crunches": crunches,
    "Triceps Dip": triceps_dip,
}


# In[31]:


# Function to start exercise based on selection
# def start_exercise():
#     exercise_index = exercise_listbox.curselection()[0]
#     repetitions = exercise_count_entry.get()
#     exercise_name = exercise_list[exercise_index]

#     if exercise_name not in exercise_functions:
#         messagebox.showerror("Error", f"{exercise_name} is not implemented.")
#         return

#     if repetitions.isdigit():
#         repetitions = int(repetitions)
#         messagebox.showinfo("Exercise", f"Starting {exercise_name} with {repetitions} repetitions.")
#         exercise_functions[exercise_name](repetitions)
#     else:
#         messagebox.showerror("Error", "Please enter a valid number for repetitions.")


# In[24]:


def start_yoga():
    global cap
    cap = cv2.VideoCapture(0)  # Initialize the webcam capture

    if not cap.isOpened():
        messagebox.showerror("Camera Error", "Failed to open camera.")
        return

    count = 0  # Counter for capturing frames
    frameloc = []  # List to store pose landmarks
    pred = ''  # Variable to store the predicted pose
    count1 = 0  # Counter for 'tree' pose
    count2 = 0  # Counter for 'goddess' pose
    count3 = 0  # Counter for 'plank' pose
    count4 = 0  # Counter for 'warrior' pose
    count5 = 0  # Counter for 'downdog' pose
    t = 200  # Threshold count for each pose

    # Initialize MediaPipe Pose with detection and tracking confidence thresholds
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()  # Read frame from webcam

            if not ret:
                print("Error: Failed to capture frame.")
                break

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert frame to RGB
            image.flags.writeable = False  # Disable frame editing to improve performance
            results = pose.process(image)  # Process the frame to detect poses
            image.flags.writeable = True  # Enable frame editing
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  # Convert frame back to BGR

            try:
                landmarks = results.pose_landmarks.landmark

                # Extract specific landmark coordinates for calculating angles
                a = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
                b = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
                c = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
                d = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                e = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                f = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                g = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
                h = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x, landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
                i = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
                j = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x, landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
                k = [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]
                l = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x, landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]

                # Check visibility of left ankle landmark
                if landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].visibility > 0.5:
                    feature = np.concatenate((a, b, c, d, e, f, g, h, i, j, k, l))
                    frameloc.append(feature)
                    count += 1

                    if count > 3:
                        # Predict poses based on captured frames
                        predictions = model.predict(frameloc)
                        print("Predictions: ", predictions)  # Debugging statement
                        frameloc = []
                        count = 0
                        predictions = list(predictions)

                        if predictions.count(3) == 4 and calculate_angle(h, j, l) < 100:
                            pred = 'tree'
                            count1 += 1
                            count2 = 0  # Reset other pose counters
                            count3 = 0
                            count4 = 0
                            count5 = 0
                        elif predictions.count(4) == 4 and calculate_angle(h, j, l) < 150 and calculate_angle(g, i, k) < 150 and count1 == t:
                            pred = 'goddess'
                            count2 += 1
                            count1 = 0  # Reset other pose counters
                            count3 = 0
                            count4 = 0
                            count5 = 0
                        elif predictions.count(2) == 4 and count2 == t:
                            pred = 'plank'
                            count3 += 1
                            count1 = 0  # Reset other pose counters
                            count2 = 0
                            count4 = 0
                            count5 = 0
                        elif predictions.count(4) == 4 and calculate_angle(g, i, k) < 150 and calculate_angle(h, j, l) > 165 and count3 == t:
                            pred = 'warrior'
                            count4 += 1
                            count1 = 0  # Reset other pose counters
                            count2 = 0
                            count3 = 0
                            count5 = 0
                        elif predictions.count(0) == 4 and calculate_angle(i, g, e) < 150 and count4 == t:
                            pred = 'downdog'
                            count5 += 1
                            count1 = 0  # Reset other pose counters
                            count2 = 0
                            count3 = 0
                            count4 = 0

            except Exception as e:
                print(f"Error processing frame: {e}")

            # Display predicted pose and landmarks on the frame
            cv2.putText(image, str(pred), (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            # Show the frame
            cv2.imshow('Yoga', image)

            # Exit the loop if 'q' is pressed or count5 reaches the threshold
            if cv2.waitKey(10) & 0xFF == ord('q') or count5 == t:
                break

        # Release the camera and close all OpenCV windows
        cap.release()
        cv2.destroyAllWindows()


# In[29]:


# # Create the main window
# root = tk.Tk()
# root.title("Exercise and Yoga Trainer")

# # Create notebook style tabs
# tab_control = ttk.Notebook(root)

# # Create tabs
# exercise_tab = ttk.Frame(tab_control)
# yoga_tab = ttk.Frame(tab_control)

# tab_control.add(exercise_tab, text='Exercise')
# tab_control.add(yoga_tab, text='Yoga')

# tab_control.pack(expand=1, fill='both')

# # Exercise Tab
# exercise_title_label = Label(exercise_tab, text="Choose an Exercise:")
# exercise_title_label.pack()

# exercise_listbox = Listbox(exercise_tab)
# exercise_listbox.pack()

# exercise_list = list(exercise_functions.keys())
# for exercise in exercise_list:
#     exercise_listbox.insert(tk.END, exercise)

# exercise_count_label = Label(exercise_tab, text="Enter Repetitions:")
# exercise_count_label.pack()

# exercise_count_entry = Entry(exercise_tab)
# exercise_count_entry.pack()

# start_exercise_button = Button(exercise_tab, text="Start Exercise", command=start_exercise)
# start_exercise_button.pack()

# # Yoga Tab
# yoga_title_label = Label(yoga_tab, text="Yoga Pose Detection")
# yoga_title_label.pack()

# start_yoga_button = Button(yoga_tab, text="Start Yoga", command=start_yoga)
# start_yoga_button.pack()

# # Run the application
# root.mainloop()


# In[ ]:




