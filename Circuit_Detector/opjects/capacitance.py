import cv2
import numpy as np
from .component import Component
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
class Capac(Component):

    com_type = 'L'

    casc = cv2.CascadeClassifier(os.path.join(current_dir, '../set/DCS2.xml'))
    scale_factor = 1.1
    min_score = 1

    state = 0

    color = (0, 255, 0)

    def init(self):
        pass

        