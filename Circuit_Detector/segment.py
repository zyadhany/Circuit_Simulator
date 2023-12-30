import cv2
import numpy as np

import editor
from opjects import *
import sys
from src.LoodDetect import CDEC
import time

#my_opjects = [Resistance(), DCS()]
my_opjects = [DCS()]

boxwire = 10
wire_lenght = 200
MAXDIFF = 10


def getnode(gray, nodes, node_map, opj):
	y, x, h, w = opj
	res = [-1, -1]
	at = 0

	for i in range(x, x + w + 1):
		if node_map[i][y] in nodes and gray[i][y]:
			if nodes[node_map[i][y]] not in res:
				res[at % 2] = nodes[node_map[i][y]]
				at += 1
		if node_map[i][y + h] in nodes and gray[i][y + h]:
			if nodes[node_map[i][y + h]] not in res:
				res[at % 2] = nodes[node_map[i][y + h]]
				at += 1
	for j in range(y, y + h + 1):
		if node_map[x][j] in nodes and gray[x][j]:
			if nodes[node_map[x][j]] not in res:
				res[at % 2] = nodes[node_map[x][j]]
				at += 1
		if node_map[x + w][j] in nodes and gray[x + w][j]:
			if nodes[node_map[x + w][j]] not in res:
				res[at % 2] = nodes[node_map[x + w][j]]
				at += 1
	return res

def CreatCircuit(gray, nodes, node_map, comp):
	circuit = []

	for opj in my_opjects:
		opj.index = 1

	for opj_itration in comp:
		opj = opj_itration[1]()
		opj.index = opj_itration[1].index
		opj_itration[1].index += 1
		opj.n1, opj.n2 = getnode(gray, nodes, node_map, opj_itration[0][1:])
	
		circuit.append(opj)
	return circuit

def simplfySkel(skel):
	n, m = skel.shape
	vis = np.zeros((n, m), dtype=int) 
	result = {}

	dic = CDEC.SimplfySkel(skel, vis, n, m)
	
	for i in range(1, dic[0].key):
		result[dic[i].key] = dic[i].val

	CDEC.free_dict(dic)
	return ([result, vis])

def IsIntersection(comp, op):

	lw = max(comp[0][1], op[0][1])
	rw = min(comp[0][1] + comp[0][3], op[0][1] + op[0][3])
	lh = max(comp[0][2], op[0][2])
	rh = min(comp[0][2] + comp[0][4], op[0][2] + op[0][4])

	if lw <= rw + MAXDIFF and lh <= rh + MAXDIFF:
		op[0][1] = min(comp[0][1], op[0][1])
		op[0][3] = max(comp[0][1] + comp[0][3], op[0][1] + op[0][3]) - op[0][1]
		op[0][2] = min(comp[0][2], op[0][2])
		op[0][4] = max(comp[0][2] + comp[0][4], op[0][2] + op[0][4]) - op[0][2]
		
		if comp[0][0] >= op[0][0]:
			op[0][0] = comp[0][0]
			op = (op[0], comp[1])
		return (op)
	
	return (0)

def AddComponent(components, op):
	going = 1

	while going:
		going = 0
		for comp in components:
			iscomp = IsIntersection(comp, op)
			if iscomp:
				going = 1
				op = iscomp
				components.remove(comp)
	components.append((op[0], op[1]))

def getComponents(src):
	skel = src.copy()
	components = []
	opj = []

	for comp in my_opjects:
		opj.extend(comp.detect(skel))
	opj.sort(reverse=True)

	for op in opj:
		AddComponent(components, op)

	for comp in components:
		x, y, w, h = comp[0][1:]
		editor.remove_part(skel, x + 1, y + 1, w - 2, h - 2)

	return [skel, components]