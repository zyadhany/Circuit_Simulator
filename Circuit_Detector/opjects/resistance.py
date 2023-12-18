import cv2
import numpy as np
from .component import Component

class Resistance(Component):
    casc = cv2.CascadeClassifier('set/res.xml')


    def init(self):
        pass


    def get_elem(self, img):
        pass
        