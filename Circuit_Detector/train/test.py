#!/usr/bin/env python3
import cv2
import pyautogui
import numpy as np

face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


while True:
    frame = pyautogui.screenshot()
    frame = np.array(frame)
    w = frame.shape[0]//2
    frame = frame[:w]
   
    
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    faces = face.detectMultiScale(gray, 1.05, 50)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
