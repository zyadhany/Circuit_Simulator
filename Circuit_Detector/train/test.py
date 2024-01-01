#!/usr/bin/env python3
import cv2
import PIL
import numpy as np
import pyautogui

face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture("vid1.mp4")

while True:
    screenshot = pyautogui.screenshot()
    frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    w = frame.shape[0] // 2
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face.detectMultiScale(gray, 1.3, 60)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break



def show_screen():

    start_time = time.time()
    frame_count = 0

    while True:


        s = time.time()
        frame = Detect_Circuit(frame)[0]
        cv2.imshow('Screen', frame)
        e = time.time()

        frame_count += 1

        # Calculate time taken for each frame
        elapsed_time = e - s
        #print("Time Taken for Frame {}: {:.2f} seconds".format(frame_count, elapsed_time))

        if cv2.waitKey(1) == ord('q'):
            break

    end_time = time.time()
    total_time = end_time - start_time
    fps = frame_count / total_time
    print("Average FPS: {:.2f}".format(fps))

    cv2.destroyAllWindows()

cv2.destroyAllWindows()
