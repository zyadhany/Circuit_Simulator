import cv2
import numpy as np
from src.LoodDetect import CDEC
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

class Component():
    casc = cv2.CascadeClassifier()

    com_type = 'comp'
    name = 'component'
    index = 1

    scale_factor = 1.05
    min_nig = 60
    min_size = (10,10)
    max_size = (120,120)

    min_score = 50
    score_factor = 1

    n1 = 0
    n2 = 0

    value = 0
    color = (0, 0, 255)

    shape = [0, 0 ,0, 0]
    score = 0

    def __init__(self):
        self.index = self.__class__.index
        self.__class__.index += 1

    def find(self, img):
        res = []
        opj = self.casc.detectMultiScale2(img, scaleFactor=self.scale_factor,
                                          minNeighbors=self.min_nig,
                                          minSize=self.min_size, maxSize=self.max_size)
        n = self.opjlen(opj)

        for i in range(n):
            score = opj[1][i]
            x, y, w, h = opj[0][i]
            xc, yc, wc, hc = self.compSize(img, x, y, w, h)
            if score >= self.min_score:
                res.append([score * self.score_factor, yc, xc, hc, wc])

        return res
    
    def detect(self, img):
        res = []
        components = self.find(img)
        for comp in components:
            opj = self.__class__()
            opj.shape = comp[1:]
            opj.score = comp[0]
            res.append(opj)
        return(res)

    def opjlen(self, opjs):
        n = 0
        for i in opjs[0]:
            n += 1
        return (n)
    
    def getNode(self, gray, nodes, node_map):
        y, x, h, w = self.shape
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
        self.n1 , self.n2 = res

    def compSize(self, img, x, y, w, h):
        arr = CDEC.CompSize(img, img.shape[0], img.shape[1], y, x, h, w)
        res = [arr[i] for i in range(4)]
        CDEC.free_array(arr)
        if res[1] == -1:
            return [0, 0]
        return res
    
    def __str__(self) -> str:
        return f'{self.com_type}{self.index} {self.n1} {self.n2} {self.value}'