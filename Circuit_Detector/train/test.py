#!/usr/bin/env python3
import numpy as np
import cv2
import pyautogui

screen_width, screen_height = pyautogui.size()

bat = cv2.CascadeClassifier('cascade/battery/cascade.xml')
res = cv2.CascadeClassifier('cascade/res.xml')


def resize(src, width=0, height=0):
    h, w = src.shape[:2]
    if not width and not height:
        return (src)

    r1, r2 = 1, 1

    if width:
        r1 = width / w
    if height:
        r2 = height / h

    if not width:
        width = w * r2
    if not height:
        height = h * r1
        
    img = cv2.resize(src, (int(width), int(height)))
    return (img)



while True:
    screen = pyautogui.screenshot()

    # Convert the screenshot to a format usable by OpenCV
    frame = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
    frame = frame[:-600]

    # frame = cv2.imread('imm.jpg')


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = bat.detectMultiScale(gray, 1.06, 50)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
        roi_gray = gray[y:y+w, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
    faces = res.detectMultiScale(gray, 1.2, 150)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 5)
        roi_gray = gray[y:y+w, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()

#
#..\..\..\opencv\build\x64\vc15\bin\opencv_createsamples.exe -info pos.txt -w 24 -h 24 -num 1000 -vec pos.vec