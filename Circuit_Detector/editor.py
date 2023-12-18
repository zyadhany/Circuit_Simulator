#!/usr/bin/env python3

import cv2
import numpy as np
    

def breakImg(src):

    img = src.copy()

    for row in range(len(img)):
        for col in range(len(img[row])):
            img[row][col] = (img[row][col] < 128) * 255
    return img


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

def draw_rectangle(img, opject):
    for op in opject:
        x, y, w, h = op[0][1:]
        cv2.rectangle(img, (x, y), (x + w, y + h), op[1].color, 5)

def remove_part(img, y, x, h, w):
    for i in range(x, x + w):
        for j in range(y, y + h):
            img[i][j] = 0