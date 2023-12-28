import tkinter as tk
from config import rootConfig, FrameBuild, headConfig
from opjects import *

root = tk.Tk()

root = rootConfig(root)

header, toolbar, content = FrameBuild(root)

header = headConfig(header)

root.mainloop()
