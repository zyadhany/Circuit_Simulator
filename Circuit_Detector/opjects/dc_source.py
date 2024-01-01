import cv2
import numpy as np
from .component import Component
from ..src.LoodDetect import CDEC
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
class DCS(Component):

    casc = cv2.CascadeClassifier(os.path.join(current_dir, '../set/DCS2.xml'))
    com_type = 'V'
    name = 'Dcs'

    scale_factor = 1.1
    min_score = 1

    state = 0

    color = (0, 255, 0)

    def detect(self, img):
        res = []
        components = self.find(img)

        for comp in components:
            x, y, width, height = comp[1:]

            roi = img[y:y+height, x:x+width]
            roi = np.ascontiguousarray(roi)

            state = CDEC.CheckDc(roi, height, width)
            
            if state:
                opj = self.__class__()
                opj.shape = comp[1:]
                opj.score = comp[0]
                opj.state = state
                res.append(opj)
        return (res)
        
    def getNode(self, gray, nodes, node_map):
        y, x, h, w = self.shape

        if self.state <= 2:
            for i in range(x, x + w + 1):
                if node_map[i][y] in nodes and gray[i][y]:
                        self.n1 = nodes[node_map[i][y]]
                if node_map[i][y + h] in nodes and gray[i][y + h]:
                        self.n2 = nodes[node_map[i][y + h]]
        else:
            for j in range(y, y + h + 1):
                if node_map[x][j] in nodes and gray[x][j]:
                        self.n1 = nodes[node_map[x][j]]
                if node_map[x + w][j] in nodes and gray[x + w][j]:
                        self.n2 = nodes[node_map[x + w][j]]
        if self.state % 2:
            self.n1, self.n2 = self.n2, self.n1
    