import cv2
import numpy as np

from . import editor
from .opjects import *
from .src.LoodDetect import CDEC
from .constant import *

my_opjects = [Resistance(), DCS(), Inductor(), Capac(), ACS(), Gnd()]
#my_opjects = [Resistance()]
NOT_CIR_COMP = [Gnd]

def FixNoding(nodes, circuit):
	cnt = 1
	tmp = {}
	rem_dict = []
	gnd = []
	
	for key, val in nodes.items():
		for comp in circuit:
			if comp.__class__ == Gnd:
				if val in comp.nodes:
					gnd.append(val)

	for key, val in nodes.items():
		keep = 0
		if val in tmp:
			continue
		if val in gnd:
			tmp[val], nodes[key] = 0, 0
			continue
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
		if comp.__class__ == Gnd:
			continue
		if comp.n1 in tmp:
			comp.n1 = tmp[comp.n1]
		if comp.n2 in tmp:
			comp.n2 = tmp[comp.n2]
		if comp.n1:
			comp.n1 = f'n{comp.n1}'
		if comp.n2:
			comp.n2 = f'n{comp.n2}'
		
def CreatCircuit(gray, nodes, node_map, components):
	circuit = []

	for opj in my_opjects:
		opj.__class__.index = 1

	for opj in components:
		if opj.__class__ == ACS:
			opj.index = DCS.index
			DCS.index += 1
		else:
			opj.index = opj.__class__.index
			opj.__class__.index += 1
		opj.getNode(gray, nodes, node_map)
		circuit.append(opj)

	FixNoding(nodes, circuit)
	for opj in circuit:
		if opj.__class__ in NOT_CIR_COMP:
			circuit.remove(opj)
	return circuit

def simplfySkel(skel, state=1):
	n, m = skel.shape
	vis = np.zeros((n, m), dtype=int) 
	result = {}

	dic = CDEC.SimplfySkel(skel, vis, n, m, state)
	
	for i in range(1, dic[0].key):
		result[dic[i].key] = dic[i].val

	CDEC.free_dict(dic)
	return ([result, vis])

def IsIntersection(comp, op):
	Inter = editor.get2dInersection(comp.shape, op.shape)
	if Inter[0][0] != -1:
		if comp.score >= op.score:
			op = comp
		op.shape = Inter[1]
		return (op)	
	return (0)

def AddComponent(components, op):
	going = 1

	while going:
		going = 0
		for comp in components:
			iscomp = IsIntersection(comp, op)
			if iscomp:
				op, going = iscomp, 1
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
