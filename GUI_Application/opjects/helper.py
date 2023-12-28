import tkinter as tk
from PIL import Image, ImageTk

def getImg(src, shape):
    w, h = shape
    img = Image.open(src).convert("RGB").resize((w, h))
    return ImageTk.PhotoImage(img)