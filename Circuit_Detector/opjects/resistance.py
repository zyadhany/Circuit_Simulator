import cv2
import numpy as np
from .component import Component

class Resistance(Component):

    name = 'res'
    casc = cv2.CascadeClassifier('set/res.xml')

    min_score = 500

    def init(self):
        pass

        