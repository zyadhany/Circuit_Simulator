#!/usr/bin/env python3

import cv2
from .src.LoodDetect import CDEC
from .constant import *

def breakImg(src):
	CDEC.BreakImg(src, src.shape[0], src.shape[1])

def applayscale(scale, img, fog=0):
	x, y, w, h = scale
	n, m = img.shape[0], img.shape[1]
	if fog:
		x -= IMAGE_SCALE_FOG
		y -= IMAGE_SCALE_FOG
		w += IMAGE_SCALE_FOG * 2
		h += IMAGE_SCALE_FOG * 2

	x, y = min(max(x, 0), m - 1), min(max(y, 0), n - 1)
	xm, ym = min(x + w, m), min(y + h, n)
	img = img[y:ym, x:xm]
	return (img)

def get2dInersection(s1, s2):
	res = []
	ls = [-1, -1, -1, -1]
	rs = [-1, -1, -1, -1]
	ls[0] = max(s1[0], s2[0])
	ls[2] = min(s1[0] + s1[2], s2[0] + s2[2])
	ls[1] = max(s1[1], s2[1])
	ls[3] = min(s1[1] + s1[3], s2[1] + s2[3])

	rs[0] = min(s1[0], s2[0])
	rs[2] = max(s1[0] + s1[2], s2[0] + s2[2]) - rs[0]
	rs[1] = min(s1[1], s2[1])
	rs[3] = max(s1[1] + s1[3], s2[1] + s2[3]) - rs[1]

	if ls[0] <= ls[2] + MIN_COMP_DIFF and ls[1] <= ls[3] + MIN_COMP_DIFF:
		ls[2] -= ls[0]
		ls[3] -= ls[1]
		res.append(ls)
	else :
		res.append([-1, -1, -1, -1])
	res.append(rs)
	return (res)

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
		lable = f'{op.name}{op.index}'
		fontscale = 0.6
		cv2.rectangle(img, (x, y), (x + w, y + h), color, 5)
		cv2.putText(img, lable, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2, cv2.LINE_AA)

def remove_part(img, y, x, h, w):
	CDEC.RemovePart(img, img.shape[0], img.shape[1], x, y, w, h)