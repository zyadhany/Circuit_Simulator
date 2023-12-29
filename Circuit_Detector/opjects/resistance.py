import cv2
import numpy as np
from .component import Component

class Resistance(Component):

    com_type = 'R'

    casc = cv2.CascadeClassifier('set/cascade.xml')
    scale_factor = 1.05
    min_score = 200
    color = (255, 0, 0)

    def init(self):
        pass

        