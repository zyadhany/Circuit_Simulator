#!/usr/bin/env python3

import cv2
import pyautogui
import numpy as np
from . import editor, segment, result

def LiveDetect():
	key = -1

	while True:
		screenshot = pyautogui.screenshot()
		frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
		#w = frame.shape[1] // 3
		w = 560
		frame = frame[200:-50,w:]
		res = Detect_Circuit(frame)
		frame = res['src']
		cv2.imshow('Screen', frame)
		#cv2.imshow('skel', res['gray'])
		key = cv2.waitKey(1)

		if key != -1:
			break
	cv2.destroyAllWindows()
	
	if key != 13:
		return (0)
	return (res)

def Detect_Circuit(src):
	res = {}

	# edit imagae to for reconizaton
	src = editor.resize(src, width=560)
	gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
	editor.breakImg(gray)
	segment.simplfySkel(gray, state=0)

	# get components and nodes
	skel, comp = segment.getComponents(gray) #35
	nodes, node_map = segment.simplfySkel(skel) #33

	# creat circuit
	circuit = segment.CreatCircuit(skel, nodes, node_map, comp)

	editor.draw_rectangle(src, circuit)

	res['gray'] = gray
	res['skel'] = skel
	res['src'] = src
	res['circuit'] = circuit
	res['nodes'], res['node_map'] = nodes, node_map
	result.BuildResult(res)
	return (res)

if __name__ == "__main__":
	LiveDetect()
