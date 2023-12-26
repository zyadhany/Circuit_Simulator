import cv2
import numpy as np

import editor
from opjects import *
import sys
from src.LoodDetect import CDEC

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



def DfsCirc(skel, vis, n, m, l, r, val):
    if l < 0 or l >= n or r < 0 or r >= m:
        return 0
    if vis[l][r] != 0 or skel[l][r] == 0:
        return 0
    len = 1
    vis[l][r] = val    

    for i in range(l - boxwire, l + boxwire + 1):
        for j in range(r - boxwire, r + boxwire + 1):
            len += DfsCirc(skel, vis, n, m, i, j, val)
    return (len)

def simplfySkel(skel):
    sys.setrecursionlimit(1000000)
    n, m = skel.shape
    vis = np.zeros((n, m), dtype=int)
    dist = {0:0}
    result = {}
    cnt = 1
    node = 1


    for i in range(n):
        for j in range(m):
            cnt += 1
            len = DfsCirc(skel, vis, n, m, i, j, cnt)
            dist[cnt] = len
   
    for i in range(n):
        for j in range(m):

            if dist[vis[i][j]] >= wire_lenght:
                if vis[i][j] not in result:
                    result[vis[i][j]] = node
                    node += 1
            else :
                skel[i][j] = 0
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
            editor.remove_part(img, x + 1, y + 1, w - 1, h - 1)

    return [img, result]