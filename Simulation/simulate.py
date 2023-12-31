#!/usr/bin/env python3

from . import ahkab
from .ahkab import new_ac, run, plotting 
from .ahkab.circuit import Circuit
import numpy as np

from .circuitCreating import CreatCir


def simulate(inp_cir, name="Circuit", info=None):
    cir = Circuit(name)

    cir = CreatCir(inp_cir, cir)

    opa = ahkab.new_op()
    r = ahkab.run(cir, opa)['op']

    