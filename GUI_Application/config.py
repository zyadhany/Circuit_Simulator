import tkinter as tk
from opjects import *
import os

current_directory = os.path.dirname(os.path.abspath(__file__))

def getPath(file_path):
    return os.path.join(current_directory, file_path)


def toggle_fullscreen(root):
    root.attributes('-fullscreen', not root.attributes('-fullscreen'))

def rootConfig(root:tk.Tk):
    
    # name and icon
    root.title("Simulation")
    root.iconbitmap(getPath("resource\icon.ico"))

    # size
    window_width = root.winfo_screenwidth()
    window_height = root.winfo_screenheight()
    root.config(width=window_width, height=window_height)
    root.minsize(1280, 720)  
    root.attributes('-fullscreen', False)
    root.bind("<F11>", lambda event:toggle_fullscreen(root))
    
    root.bind("<q>", lambda event:root.quit())

    return root

def headConfig(header:tk.Tk):
    run = Button(header)
    button.pack(expand=True, padx=10, pady=10)  # Add padding for better visualization
    run.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    run.pack()
    return header


def FrameBuild(root:tk.Tk):
    window_width = root.winfo_screenwidth()
    window_height = root.winfo_screenheight()

    # grid gemo
    w_head = int(window_width * 0.9)
    h_head = int(window_height * 0.1)
    gc_head = 50
    gr_head = 2

    h_content = window_height - w_head
    gc_content = gc_head
    gr_content = 50

    w_tool = window_width - w_head
    gc_tool = 5
    gr_tool = gr_head + gr_content

    # Header Frame
    header = tk.Frame(root, height=h_head, width=w_head, bg='blue')
    header.grid(row=0, column=0, columnspan=gc_head, rowspan=gr_head, sticky='ew')
    
    # Toolbar Frame
    toolbar = tk.Frame(root, height=window_height, width=w_tool, bg='red')
    toolbar.grid(row=0, column=gc_head, columnspan=gc_tool, rowspan=gr_tool, sticky='ns')

    # Main Content Frame
    content = tk.Frame(root, height=h_content, width=w_head, bg='green')
    content.grid(row=gr_head, column=0, rowspan=gr_content, columnspan=gc_content, sticky='nsew')

    header.pack_propagate(False)
    toolbar.pack_propagate(False)
    content.pack_propagate(False)

    return([header, toolbar, content])
