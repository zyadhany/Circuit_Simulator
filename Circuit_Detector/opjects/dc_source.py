import cv2
import numpy as np
from .component import Component
from ..src.LoodDetect import CDEC
from .capacitance import Capac
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
class DCS(Component):
    com_type = 'V'
    name = 'V'
    color = (0, 255, 0)

    val_ac = 0
    type = 'dc'
    state = 0

    casc = cv2.CascadeClassifier(os.path.join(current_dir, '../set/DCS2.xml'))
    scale_factor = 1.1
    min_score = 1



    def detect(self, img):
        res = []
        components = self.find(img)

        for comp in components:
            x, y, width, height = comp[1:]

            roi = img[y:y+height, x:x+width]
            roi = np.ascontiguousarray(roi)

            state = CDEC.CheckDc(roi, height, width)

            if state:
                if state == 5:
                    opj = Capac()
                else:
                    opj = self.__class__()
                    opj.state = state
                opj.shape = comp[1:]
                opj.score = comp[0]
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
