import cv2
import numpy as np
from .component import Component
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
class Inductor(Component):

    com_type = 'L'

    casc = cv2.CascadeClassifier(os.path.join(current_dir, '../set/ind.xml'))
    scale_factor = 1.3

    min_score = 1
    color = (150, 120, 0)

    score_factor = 20

    def init(self):
        pass

        