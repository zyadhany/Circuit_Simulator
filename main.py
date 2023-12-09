#!/usr/bin/env python3


import models.ahkab as ahkab
from models.ahkab import new_op, run, plotting 
from models.ahkab.circuit import Circuit
import numpy as np


# Define the circuit
mycir = ahkab.Circuit('Butterworth 1kHz band-pass filter', filename='crr')
mycir.add_resistor('R1', 'n1', mycir.gnd, value=5)
mycir.add_vsource('V1', 'n2', 'n1', dc_value=8)
mycir.add_resistor('R2', 'n2', mycir.gnd, value=2)
mycir.add_vsource('V2', 'n3', 'n2', dc_value=4)
mycir.add_resistor('R3', 'n3', mycir.gnd, value=4)
mycir.add_resistor('R4', 'n3', 'n4', value=1)
mycir.add_vsource('V3', 'n4', mycir.gnd, dc_value=10)
mycir.add_resistor('R5', 'n2', 'n4', value=4)

# Define the analysis
op = new_op()

res = run(mycir, op)

#plotting.plot_results('3th order 1kHz Butterworth filter', [('|Vn6|',"")], res['ac'])
plotting.show_plots()