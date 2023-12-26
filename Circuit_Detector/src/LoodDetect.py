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

#array
CDEC.free_array.argtypes = [ctypes.POINTER(ctypes.c_int)]