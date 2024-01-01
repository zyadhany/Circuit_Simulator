import cv2
import numpy as np
from .component import Component
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
class Resistance(Component):
	com_type = 'R'
	name = 'R'
	color = (255, 0, 0)

	casc = cv2.CascadeClassifier(os.path.join(current_dir, '../set/res3.xml'))
	scale_factor = 1.3
	min_score = 10
	score_factor = 5
