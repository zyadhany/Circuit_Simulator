#!/usr/bin/env python3
import numpy as np
import cv2
import time

res = cv2.CascadeClassifier('cascade/resistor/cascade.xml')
res2 = cv2.CascadeClassifier('cascade/resistor/res.xml')
bat = cv2.CascadeClassifier('cascade/battery/cascade.xml')


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



frame = cv2.imread('imm.jpg')
frame = resize(frame, height=720)
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

r = res.detectMultiScale2(gray, 1.2, 200)
start = time.time()
r = res.detectMultiScale2(gray, 1.3, 60)
end = time.time()
print(f"Time is: {end - start}")


start = time.time()
d = res2.detectMultiScale2(gray, 1.3, 60)
end = time.time()
print(f"Time is: {end - start}")

sr = 300
sd = 300

n = 0
for i in r[0]:
    n+=1
for i in range(n):
    x, y, w, h = r[0][i]
    print(r[1][i])
    if r[1][i] >= sr:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 5)
        roi_gray = gray[y:y+w, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

n = 0
for i in d[0]:
    n+=1
for i in range(n):
    x, y, w, h = d[0][i]
    print(d[1][i])
    if d[1][i] >= sd:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
        roi_gray = gray[y:y+w, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

cv2.imshow('frame', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
