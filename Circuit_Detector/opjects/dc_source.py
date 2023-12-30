import cv2
import numpy as np
from .component import Component
from src.LoodDetect import CDEC

class DCS(Component):

    casc = cv2.CascadeClassifier('set/DCS2.xml')
    com_type = 'DCS'
    name = 'Dcs'

    scale_factor = 1.15
    min_score = 1

    color = (0, 255, 0)

    def detect(self, img):
        compon = self.find(img)

        for comp in compon:
            x, y, width, height = comp[0][1:]

            roi = img[y:y+height, x:x+width]
            roi = np.ascontiguousarray(roi)

            re = CDEC.CheckDc(roi, width, height)
            if not re:
                compon.remove(comp)
        return (compon)
    

        