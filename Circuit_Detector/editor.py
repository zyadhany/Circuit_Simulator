#!/usr/bin/env python3

import cv2
import numpy as np
from .src.LoodDetect import CDEC

def breakImg(src):
    CDEC.BreakImg(src, src.shape[0], src.shape[1])

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
        x, y, w, h = op.shape
        color = op.color
        lable = f'{op.com_type}{op.index}'
        fontscale = 0.6
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 5)
        cv2.putText(img, lable, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2, cv2.LINE_AA)

def remove_part(img, y, x, h, w):
    CDEC.RemovePart(img, img.shape[0], img.shape[1], x, y, w, h)