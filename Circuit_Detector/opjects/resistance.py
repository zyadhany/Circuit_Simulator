import cv2
import numpy as np
from .component import Component
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
class Resistance(Component):

    com_type = 'R'
    name = 'Res'

    casc = cv2.CascadeClassifier(os.path.join(current_dir, '../set/res3.xml'))
    scale_factor = 1.3

    min_score = 10
    color = (255, 0, 0)

    score_factor = 5

    def init(self):
        pass

        