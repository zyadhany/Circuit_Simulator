#!/usr/bin/env python3

import cv2
import numpy as np

import editor

def getline(src):

    img = src.copy()

    for row in range(len(img)):
        for col in range(len(img[row])):
            img[row][col] = (img[row][col] < 128) * 255  # Modify pixel value based on condition
    return img

def Detect_Circuit(img_file):
    res = {}

    src = cv2.imread(img_file)

    
    src = editor.resize(src, height=720)
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    gray = getline(gray)

    cv2.imwrite("imm.jpg", img=gray)
    cv2.imshow("res", gray)
    cv2.waitKey(0)

    return (res)


if __name__ == "__main__":
    Detect_Circuit("img1.jpg")