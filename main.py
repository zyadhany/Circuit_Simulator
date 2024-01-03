import tkinter as tk
from GUI_Application import *
from console import SimulationCommand



def main():
    sc = SimulationCommand()
    root = tk.Tk()
    components = []
    sc.tkr = root
    root = rootConfig(root)
    Main = tk.Frame(root)
    header, content = FrameBuild(Main)

    DET, RUN = headConfig(header)
    ADD, RESET, bar, compBox = contentConfig(content)


    DET.config(command=lambda sc=sc, cmp=components, fr=compBox: detect(sc, cmp, fr))
    RUN.config(command=lambda sc=sc, cmp=components: run(sc, cmp))
    ADD.config(command=lambda fr=compBox, cmp=components: add(fr, cmp))
    RESET.config(command=lambda sc=sc, cmp=components: reset(sc, cmp))
    #root.destroy()
    Main.pack()
    root.mainloop()

if __name__ == "__main__":
    main()