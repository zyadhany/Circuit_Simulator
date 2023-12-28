import cv2
import numpy as np
from src.LoodDetect import CDEC

class Component():

    com_type = 'comp'

    name = 1

    casc = cv2.CascadeClassifier('set/res.xml')

    scale_factor = 1.05
    min_nig = 60

    min_score = 500

    com_w = 40
    com_h = 20

    n1 = 0
    n2 = 0

    value = 0

    color = (0, 0, 255)

    def __init__(self):
        pass

    def find(self, img):
        res = []
        opj = self.casc.detectMultiScale2(img, scaleFactor=self.scale_factor,
                                          minNeighbors=self.min_nig)
        n = self.opjlen(opj)

        for i in range(n):
            score = opj[1][i]
            x, y, w, h = opj[0][i]
            xc, yc, wc, hc = self.compSize(img, x, y, w, h)
            if score >= self.min_score and(
                (wc >= self.com_w and hc >= self.com_h) or (wc >= self.com_h and hc >= self.com_w)):
                #print(score, self.min_score)
                res.append(([score, yc, xc, hc, wc],self.__class__))

        return res
    
    def detect(self, img):
        return(self.find(img))

    def opjlen(self, opjs):
        n = 0
        for i in opjs[0]:
            n += 1
        return (n)
    
    def compSize(self, img, x, y, w, h):

        arr = CDEC.CompSize(img, img.shape[0], img.shape[1], y, x, h, w)
        res = [arr[i] for i in range(4)]
        CDEC.free_array(arr)
        if res[1] == -1:
            return [0, 0]
        return res
    
    def __str__(self) -> str:
        return f'{self.com_type}{self.name} {self.n1} {self.n2} {self.value}'