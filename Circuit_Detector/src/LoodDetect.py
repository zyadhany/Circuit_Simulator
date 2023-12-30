#!/usr/bin/env python3

import ctypes
import numpy as np

CDEC = ctypes.CDLL("./src/Detect.dll")

#edit
CDEC.BreakImg.argtypes = [np.ctypeslib.ndpointer(dtype=np.uint8, ndim=2, flags='C_CONTIGUOUS'),
                          ctypes.c_int, ctypes.c_int]
CDEC.RemovePart.argtypes = [np.ctypeslib.ndpointer(dtype=np.uint8, ndim=2, flags='C_CONTIGUOUS'),
                          ctypes.c_int, ctypes.c_int,
                          ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]

#segment
CDEC.CompSize.argtypes = [np.ctypeslib.ndpointer(dtype=np.uint8, ndim=2, flags='C_CONTIGUOUS'),
                          ctypes.c_int, ctypes.c_int,
                          ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
CDEC.CompSize.restype = ctypes.POINTER(ctypes.c_int)

class Dict(ctypes.Structure):
    _fields_ = [("key", ctypes.c_int),
                ("val", ctypes.c_int)]

CDEC.SimplfySkel.argtypes = [np.ctypeslib.ndpointer(dtype=np.uint8, ndim=2, flags='C_CONTIGUOUS'),
                             np.ctypeslib.ndpointer(dtype=np.int32, ndim=2, flags='C_CONTIGUOUS'),
                             ctypes.c_int,
                             ctypes.c_int]

CDEC.SimplfySkel.restype = ctypes.POINTER(Dict)

#component
CDEC.CheckDc.argtypes = [np.ctypeslib.ndpointer(dtype=np.uint8, ndim=2, flags='C_CONTIGUOUS'),
                          ctypes.c_int, ctypes.c_int]

CDEC.CheckDc.restype = ctypes.c_int


#array
CDEC.free_array.argtypes = [ctypes.POINTER(ctypes.c_int)]
CDEC.free_dict.argtypes = [ctypes.POINTER(Dict)]
