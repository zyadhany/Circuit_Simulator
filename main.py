#!/usr/bin/env python3

import cv2
from Circuit_Detector import *

from Simulation import *
from Simulation.ahkab.netlist_parser import parse_circuit



result = LiveDetect()

for i in result['circuit']:
    print(i)

cv2.imshow('res', result['srcScale'])
cv2.waitKey(0)
#simulate()