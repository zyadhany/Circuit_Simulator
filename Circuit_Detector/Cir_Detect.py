#!/usr/bin/env python3

import cv2
import numpy as np
import editor
import segment


def Detect_Circuit(src):
	res = {}
	src = editor.resize(src, height=720)
	gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
	editor.breakImg(gray)

	#return ([gray, 1]) 
	skel, comp = segment.getComponents(gray) #869
	nodes, node_map = segment.simplfySkel(skel) #52
	#cv2.imshow("ime", skel)
	circuit = segment.CreatCircuit(skel, nodes, node_map, comp)

	editor.draw_rectangle(src, comp)

	return ([src, circuit])


if __name__ == "__main__":
	img = cv2.imread("img5.jpg")
	res, cir = Detect_Circuit(img)
	res, cir = Detect_Circuit(img)

	for op in cir:
		print(op)    
	cv2.imshow('res', res)
	cv2.waitKey(0)
