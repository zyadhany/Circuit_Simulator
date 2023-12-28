import cv2
import numpy as np

import editor
from opjects import *
import sys
from src.LoodDetect import CDEC
import time

my_opjects = [Resistance(), DCS()]

boxwire = 10
wire_lenght = 200

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

    for opj_itration in comp:
        opj = opj_itration[1]()
        opj.name = opj_itration[1].name
        opj_itration[1].name += 1
        opj.n1, opj.n2 = getnode(gray, nodes, node_map, opj_itration[0][1:])
    
        circuit.append(opj)
    return circuit

def simplfySkel(skel):
    n, m = skel.shape
    vis = np.zeros((n, m), dtype=int) 
    result = {}

    import time
    dic = CDEC.SimplfySkel(skel, vis, n, m)

    for i in range(1, dic[0].key):
        result[dic[i].key] = dic[i].val

    CDEC.free_dict(dic)
    return ([result, vis])

def getComponents(src):
    result = []
    img = src.copy()

    going = 1
    while going:
        going = 0
        mx , index = -1, -1
        opj = []

        for comp in my_opjects:
            opj.extend(comp.detect(img))

        for i in range(len(opj)):
            if opj[i][0][0] > mx:
                mx, index = opj[i][0][0], i

        if index >= 0:
            going = 1
            result.append((opj[index][0], opj[index][1]))
            x, y, w, h = opj[index][0][1:]
            editor.remove_part(img, x + 1, y + 1, w - 2, h - 2)

    return [img, result]