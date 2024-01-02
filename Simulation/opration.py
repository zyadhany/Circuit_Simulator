from . import ahkab
from .ahkab import run, new_ac, new_op,plotting 
from .ahkab.circuit import Circuit
import numpy as np


def op(op, cir):
    op = new_op()
    return (op)

def ac(op, cir):
    op = new_ac()
    return (op)

OPRATION = {
    'op': op, 'ac':ac
}

def runCir(op, cir):
    found = 0

    if op[0] not in OPRATION:
        print("opration not found")
        return None
    
    opration = OPRATION[op[0]](op[1:], cir)
    res = run(cir, opration)

    return (res)