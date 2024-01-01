import cv2
import numpy as np
from .component import Component
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
class Capac(Component):
    com_type = 'C'
    name = 'C'
    color = (0, 0, 255)

    casc = cv2.CascadeClassifier(os.path.join(current_dir, '../set/DCS2.xml'))
    scale_factor = 1.1
    min_score = 1

    def init(self):
        pass

    def detect(self, img):
        return []
        