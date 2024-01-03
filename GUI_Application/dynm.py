import tkinter as tk
from .compframe import compFrame
from console import SimulationCommand, BuildCirc


def run(sc:SimulationCommand, components):
    sc.do_reset()
    net = []
    for comp in components:
        net.append(str(comp))
    BuildCirc(net, sc)
    sc.do_run()

def detect(sc, components, fr):
    reset(sc, components)
    sc.do_detect(itrateValue=0)
    for comp in sc.net:
        c = compFrame(fr, components)
        c.build_from_str(str(comp))

def reset(sc, components=[]):
    sc.do_reset()
    while len(components):
        components[-1].destroy()

def add(fr, component=[]):
    comp = compFrame(fr,component)
    pass