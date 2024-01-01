import cv2
import numpy as np

from . import editor
from .opjects import *
from .src.LoodDetect import CDEC

my_opjects = [Resistance(), DCS() , Inductor()]
#my_opjects = [Inductor()]

boxwire = 10
wire_lenght = 200
MAXDIFF = 10

def FixNoding(nodes, circuit):
	cnt = 1
	tmp = {}
	rem_dict = []

	for key, val in nodes.items():
		keep = 0
		for comp in circuit:
			if val == comp.n1 or val == comp.n2:
				tmp[val], nodes[key] = cnt, cnt
				cnt += 1
				keep = 1
				break
		if not keep:
			rem_dict.append(key)
	for key in rem_dict:
		del nodes[key]
	for comp in circuit:
		if comp.n1 in tmp:
			comp.n1 = tmp[comp.n1]
		if comp.n2 in tmp:
			comp.n2 = tmp[comp.n2]

def CreatCircuit(gray, nodes, node_map, components):
	circuit = []

	for opj in my_opjects:
		opj.__class__.index = 1

	for opj in components:
		opj.index = opj.__class__.index
		opj.__class__.index += 1
		opj.getNode(gray, nodes, node_map)
		circuit.append(opj)

	FixNoding(nodes, circuit)
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

	s1 = comp.shape
	s2 = op.shape

	lw = max(s1[0], s2[0])
	rw = min(s1[0] + s1[2], s2[0] + s2[2])
	lh = max(s1[1], s2[1])
	rh = min(s1[1] + s1[3], s2[1] + s2[3])

	if lw <= rw + MAXDIFF and lh <= rh + MAXDIFF:
		s2[0] = min(s1[0], s2[0])
		s2[2] = max(s1[0] + s1[2], s2[0] + s2[2]) - s2[0]
		s2[1] = min(s1[1], s2[1])
		s2[3] = max(s1[1] + s1[3], s2[1] + s2[3]) - s2[1]
		
		if comp.score >= op.score:
			op = comp
			op.shape = s2
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
	components.append(op)

def getComponents(src):
	skel = src.copy()
	components = []
	opj = []

	for comp in my_opjects:
		opj.extend(comp.detect(skel))
	for op in opj:
		AddComponent(components, op)
	for comp in components:
		x, y, w, h = comp.shape
		editor.remove_part(skel, x + 1, y + 1, w - 2, h - 2)

	return [skel, components]
