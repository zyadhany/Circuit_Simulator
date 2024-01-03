import ahkab
from ahkab import new_op, run
from ahkab.circuit import Circuit
from ahkab.plotting import plot_results # calls matplotlib for you
import numpy as np

# Define the circuit
cir = Circuit('Butterworth 1kHz band-pass filter')
cir.add_vsource('V1', 'n1', cir.gnd, dc_value=10.)
cir.add_resistor('R1', 'n1', cir.gnd, 5.)


ac1 = new_op()

res = run(cir, ac1)

print(res['op'])