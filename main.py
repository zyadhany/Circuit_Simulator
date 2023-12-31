#!/usr/bin/env python3

from Circuit_Detector import *
from Simulation import *
from Simulation.ahkab.netlist_parser import parse_circuit

result = LiveDetect()

simulate(result['circuit'])