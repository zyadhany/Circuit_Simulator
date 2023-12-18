#!/usr/bin/env python3

import cv2
import numpy as np

import editor
import segment

# Time -> (BreakImg)

def Detect_Circuit(img_file):
    res = {}

    src = cv2.imread(img_file)

    
    src = editor.resize(src, height=720)
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    gray = editor.breakImg(gray)

    comp = segment.getComponents(gray)
    

    cv2.imshow("res", comp)
    cv2.waitKey(0)

    return (res)


if __name__ == "__main__":
    Detect_Circuit("img1.jpg")