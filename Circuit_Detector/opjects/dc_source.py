import cv2
import numpy as np
from .component import Component

class DCS(Component):

    com_type = 'DCS'
    casc = cv2.CascadeClassifier('set/dcs.xml')

    min_score = 150
    color = (0, 255, 0)

    def init(self):
        pass

        