import cv2
from .component import Component
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
class Inductor(Component):
    com_type = 'L'
    name = 'L'
    color = (150, 120, 0)

    casc = cv2.CascadeClassifier(os.path.join(current_dir, '../set/ind.xml'))
    scale_factor = 1.3
    min_score = 10
    score_factor = 5
