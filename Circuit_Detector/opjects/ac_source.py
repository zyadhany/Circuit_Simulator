import cv2
from .component import Component
from ..src.LoodDetect import CDEC
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
class ACS(Component):
    com_type = 'V'
    name = 'Vc'
    color = (0, 125, 125)

    val_ac = 0
    type = 'ac'

    casc = cv2.CascadeClassifier(os.path.join(current_dir, '../set/ACS2.xml'))
    scale_factor = 1.05
    min_score = 1
    score_factor = 1000
