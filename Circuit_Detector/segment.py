import cv2
import numpy as np

import editor
from opjects import *


def getComponents(img):
    result = {}
    faces = Resistance.casc.detectMultiScale(img, 1.2, 150)
    print(faces)

    return faces
    going = 1
    while going:
        pass

    return (result)