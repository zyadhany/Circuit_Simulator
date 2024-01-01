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

    def init(self):
        pass

        