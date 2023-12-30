import cv2
import numpy as np
from .component import Component

class Resistance(Component):

    com_type = 'R'

    casc = cv2.CascadeClassifier('set/res3.xml')
    scale_factor = 1.3
    min_nig = 60
    min_score = 10
    color = (255, 0, 0)

    score_factor = 5

    def init(self):
        pass

        