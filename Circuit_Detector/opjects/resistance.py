import cv2
import numpy as np
from .component import Component

class Resistance(Component):

    com_type = 'R'

    casc = cv2.CascadeClassifier('set/res.xml')

    min_score = 500
    color = (255, 0, 0)

    def init(self):
        pass

        