#!/usr/bin/env python3

import cv2
import numpy as np
import editor
import segment

# Time -> (BreakImg)

def Detect_Circuit(src):
    res = {}
    src = editor.resize(src, height=360)

    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    editor.breakImg(gray)

    skel, comp = segment.getComponents(gray)

    nodes, node_map = segment.simplfySkel(skel)

    circuit = segment.CreatCircuit(skel, nodes, node_map, comp)

    editor.draw_rectangle(src, comp)

    return ([src, circuit])


if __name__ == "__main__":
    img = cv2.imread("img1.jpg")
    res, cir = Detect_Circuit(img)
    for op in cir:
        print(op)    
    cv2.imshow('res', res)
    cv2.waitKey(0)
