#!/usr/bin/env python3

from .ahkab.circuit import Circuit

def addres(comp, cir:Circuit):
    name = f'{comp.com_type}{comp.index}'
    val = comp.value
    cir.add_resistor(name, n1=f'n{comp.n1}', n2=f'n{comp.n2}', value=1)

def addDcs(comp, cir:Circuit):
    name = f'{comp.com_type}{comp.index}'
    cir.add_vsource(name, n1=f'n{comp.n1}', n2=cir.gnd, dc_value=comp.value)


COMP_MAPING = {'R': addres, 'V' : addDcs}

def CreatCir(inp_cir, cir:Circuit):
    cir.add_resistor('R1', 'n1', cir.gnd, value=5)
    cir.add_vsource('V1', 'n2', 'n1', dc_value=8)
    cir.add_resistor('R2', 'n2', cir.gnd, value=2)
    cir.add_vsource('V2', 'n3', 'n2', dc_value=4)
    cir.add_resistor('R3', 'n3', cir.gnd, value=4)
    cir.add_resistor('R4', 'n3', 'n4', value=1)
    cir.add_vsource('V3', 'n4', cir.gnd, dc_value=10)
    cir.add_resistor('R5', 'n2', 'n4', value=4)
    return cir
    for comp in inp_cir:
        COMP_MAPING[comp.com_type](comp, cir)
