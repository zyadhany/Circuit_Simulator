import cv2
import numpy as np

import editor
from opjects import *

my_opjects = [Resistance()]

def getComponents(src):
    result = {}
    img = src.copy()

    going = 1
    while going:
        going = 0
        mx , index = -1, -1
        opj = []

        for comp in my_opjects:
            opj.extend(comp.find(img))

        for i in range(len(opj)):
            if opj[i][0][0] > mx:
                mx, index = opj[i][0][0], i

        if index >= 0:
            going = 1
            result[opj[index][1]] = opj[index][0]
            x, y, w, h = opj[index][0][1:]
            editor.remove_part(img, x, y, w, h)

    return (img)