import cv2
import numpy as np

class Component():

    name = 'comp'

    casc = cv2.CascadeClassifier('set/res.xml')

    scale_factor = 1.05
    min_nig = 60

    min_score = 500

    def init(self):
        pass
    

    def find(self, img):
        res = []
        opj = self.casc.detectMultiScale2(img, scaleFactor=self.scale_factor,
                                          minNeighbors=self.min_nig)
        
        n = self.opjlen(opj)

        for i in range(n):
            score = opj[1][i]
            x, y, w, h = opj[0][i]
            if score >= self.min_score:
                res.append(([score, x, y, w, h],self.name))
        return res
    
    def opjlen(self, opjs):
        n = 0
        for i in opjs[0]:
            n += 1
        return (n)