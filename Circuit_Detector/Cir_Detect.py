#!/usr/bin/env python3

import cv2
import numpy as np
import editor
import segment
import time


def Detect_Circuit(src):

	# edit imagae to for reconizaton
	src = editor.resize(src, height=560)
	gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
	editor.breakImg(gray)

	skel, comp = segment.getComponents(gray) #869
	nodes, node_map = segment.simplfySkel(skel) #52
	circuit = segment.CreatCircuit(skel, nodes, node_map, comp)

	editor.draw_rectangle(src, comp)

	return ([src, circuit])


if __name__ == "__main__":
	for i in range(1,6):
		img = cv2.imread(f"img_test/img{i}.jpg")
		start = time.time()
		res, cir = Detect_Circuit(img)
		end = time.time()
		print("Time Taken: ", (end - start) * 1000)

		for op in cir:
			print(op)    
		cv2.imshow('res', res)
		cv2.waitKey(0)
