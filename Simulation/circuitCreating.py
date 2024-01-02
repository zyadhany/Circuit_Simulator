#!/usr/bin/env python3

from .ahkab.circuit import Circuit
from . import error

def GetValue(str):
    if type(str) == 'float':
        return str
    val = float(str)
    return val

def addres(net, cir:Circuit):
    if len(net) != 4:
        print(error.RES_NET_ERROR_USAGE)
        return
    cir.add_resistor(net[0], n1=net[1], n2=net[2], value=GetValue(net[3]))

def addcap(net, cir:Circuit):
    if len(net) != 4:
        print(error.RES_NET_ERROR_USAGE)
        return
    cir.add_capacitor(net[0], n1=net[1], n2=net[2], value=GetValue(net[3]))

def addind(net, cir:Circuit):
    if len(net) != 4:
        print(error.RES_NET_ERROR_USAGE)
        return
    cir.add_inductor(net[0], n1=net[1], n2=net[2], value=GetValue(net[3]))

def addDcs(net, cir:Circuit):
    if len(net) < 4:
        print(error.DCS_NET_ERROR_USAGE)
        return
    
    vdc, vac = 0, 0
    for i in range(3, len(net)):
        if "dc=" in net[i]:
            vdc = GetValue(net[i][3:])
        if "ac=" in net[i]:
            vac = GetValue(net[i][3:])

    cir.add_vsource(net[0], n1=net[1], n2=net[2], dc_value=vdc, ac_value=vac)

COMP_MAPING = {'R':addres, 'V':addDcs, 'C':addcap, 'L':addind}

def CreatCir(inp_cir, cir:Circuit):
    for comp in inp_cir:
        COMP_MAPING[comp.com_type](str(comp), cir)
    return cir
