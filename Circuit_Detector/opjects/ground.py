import cv2
import numpy as np
from .component import Component
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
class Gnd(Component):
    com_type = 'gnd'
    name = 'gnd'
    color = (60, 60, 200)

    casc = cv2.CascadeClassifier(os.path.join(current_dir, '../set/gnd2.xml'))
    scale_factor = 1.3
    min_score = 10
    score_factor = 5

    nodes = []

    def getNode(self, gray, nodes, node_map):
        y, x, h, w = self.shape

        for i in range(x, x + w + 1):
            if node_map[i][y] in nodes and gray[i][y]:
                if nodes[node_map[i][y]] not in self.nodes:
                    self.nodes.append(nodes[node_map[i][y]])
            if node_map[i][y + h] in nodes and gray[i][y + h]:
                if nodes[node_map[i][y + h]] not in self.nodes:
                    self.nodes.append(nodes[node_map[i][y + h]])

        for j in range(y, y + h + 1):
            if node_map[x][j] in nodes and gray[x][j]:
                if nodes[node_map[x][j]] not in self.nodes:
                    self.nodes.append(nodes[node_map[x][j]])
            if node_map[x + w][j] in nodes and gray[x + w][j]:
                if nodes[node_map[x + w][j]] not in self.nodes:
                    self.nodes.append(nodes[node_map[x + 2][j]])
