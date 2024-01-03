import tkinter as tk
import os
from .opjects import *
from .compframe import compFrame

current_directory = os.path.dirname(os.path.abspath(__file__))

def getPath(file_path):
    return os.path.join(current_directory, file_path)


def toggle_fullscreen(root):
    root.attributes('-fullscreen', not root.attributes('-fullscreen'))

def rootConfig(root:tk.Tk):
    
    # name and icon
    root.title("Simulation")
    root.iconbitmap(getPath("resource/icon.ico"))

    # size
    window_width = root.winfo_screenwidth()
    window_height = root.winfo_screenheight()
    root.config(width=500, height=720)

    root.attributes('-fullscreen', False)
    root.bind("<F11>", lambda event:toggle_fullscreen(root))
    root.bind("<Escape>", lambda event:root.quit())

    return root

def headConfig(header:tk.Tk):

    DET = Button(header, text='DET')
    DET.shape = [40, 40]
    DET.bg_image = getPath('resource/DET.jpeg')
    DET.pack(side=tk.LEFT, padx=(70, 20), pady=10)
    
    RUN = Button(header, text='RUN')
    RUN.shape = [40, 40]
    RUN.bg_image = getPath('resource/run.jpg')
    RUN.pack(side=tk.RIGHT, padx=(20, 70), pady=10)

    return [DET, RUN]

def contentConfig(content:tk.Tk):
    
    # TOP BAR
    bar = tk.Frame(content)
    ADD = Button(bar, text='ADD')
    ADD.pack(side=tk.LEFT, padx=(20, 70), pady=10)
    RESET = Button(bar, text='RESET')
    RESET.pack(side=tk.RIGHT, padx=(70, 20), pady=10)
    bar.pack()

    compBox = tk.Frame(content)
    compBox.pack(fill=tk.X)
    return [ADD, RESET, bar, compBox]

def FrameBuild(root:tk.Tk):
    window_width = root.winfo_screenwidth()
    window_height = root.winfo_screenheight()

    # grid geometry
    w_head = int(window_width // 3)
    h_head = int(window_height * 0.1)
    gc_head = 2
    gr_head = 1

    h_content = window_height - h_head
    w_content = int(window_width)
    gc_content = 1
    gr_content = 1

    # Header Frame
    header = tk.Frame(root, height=h_head, width=w_head, bg='#DBA159')
    header.grid(row=0, column=0, columnspan=gc_head, rowspan=gr_head, sticky='ew')

    # Main Content Frame
    content = tk.Frame(root, height=h_content, width=w_head, bg='white')
    content.grid(row=gr_head, column=0, rowspan=gr_content, columnspan=gc_content, sticky='nsew')

    header.pack_propagate(False)
    content.pack_propagate(False)

    return([header, content])
