#!/usr/bin/env python3

import cv2

import numpy as np

import editor

import segment

# Time -> (BreakImg)

def Detect_Circuit(img_file):
    print("Detectiong in on")
    res = {}

    src = cv2.imread(img_file)

    src = editor.resize(src, height=720)

    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    gray = editor.breakImg(gray)

    skel, comp = segment.getComponents(gray)

    nodes, node_map = segment.simplfySkel(skel)

    circuit = segment.CreatCircuit(skel, nodes, node_map, comp)

    for op in circuit:
        print(op)

    editor.draw_rectangle(src, comp)
    cv2.imshow("res", src)

    cv2.waitKey(0) 

    return (res)


if __name__ == "__main__":
    Detect_Circuit("img2.jpg")
