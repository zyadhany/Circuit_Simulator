#!/usr/bin/env python3

import cv2
import pyautogui
import numpy as np
import time
from . import editor, segment


def LiveDetect():
	key = -1

	while True:
		screenshot = pyautogui.screenshot()
		frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
		w = frame.shape[1] // 3
		frame = frame[:,w:]
		res = Detect_Circuit(frame)
		frame = res['src']
		cv2.imshow('Screen', frame)
		cv2.imshow('skel', res['gray'])
		key = cv2.waitKey(1)

		if key == ord('q'):
			break
		elif key != -1:
			res = 0
			break

	cv2.destroyAllWindows()
	return (res)

def Detect_Circuit(src):
	result = {}

	# edit imagae to for reconizaton
	src = editor.resize(src, width=720)
	gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
	editor.breakImg(gray)
	segment.simplfySkel(gray, state=0)

	# get components and nodes
	skel, comp = segment.getComponents(gray) #35
	nodes, node_map = segment.simplfySkel(skel) #33

	# creat circuit
	circuit = segment.CreatCircuit(skel, nodes, node_map, comp)

	editor.draw_rectangle(src, comp)

	result['skel'] = skel
	result['gray'] = gray
	result['src'] = src
	result['circuit'] = circuit
	return (result)


if __name__ == "__main__":
	LiveDetect()
	exit()
	img = cv2.imread(f"img_test/img6.jpg")
	res = Detect_Circuit(img)
	start = time.time()
	res = Detect_Circuit(img)
	end = time.time()
	print("Time Taken: ", (end - start) * 1000)

	cv2.imshow('res', res['src'])
	cv2.waitKey(0)
