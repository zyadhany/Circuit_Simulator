import cv2
import numpy as np
from . import editor
from .src.LoodDetect import CDEC

def circuitScale(nodes, node_map, circuit):
    if not len(circuit):
        return ([0, 0, 1, 1])

    scale = []
    node_tmp = []
    for key in nodes.keys():
        node_tmp.append(key)
    node_tmp = np.array(node_tmp, dtype=int)
    
    sc = CDEC.nodeScale(node_tmp, node_map, node_map.shape[0], node_map.shape[1], node_tmp.size) 
    scale = [sc[i] for i in range(4)]

    if scale[2] <= 0 or scale[3] <= 0:
        scale = circuit[0].shape

    CDEC.free_array(sc)

    for comp in circuit:
        scale = editor.get2dInersection(scale, comp.shape)[1]
    return (scale)

def BuildResult(res):
    sclae = circuitScale(res['nodes'], res['node_map'], res['circuit'])
    res['srcScale'] = editor.applayscale(sclae, res['src'], fog=1)
    res['grayScale'] = editor.applayscale(sclae, res['gray'], fog=1)
    pass