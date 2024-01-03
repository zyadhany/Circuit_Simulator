import tkinter as tk
import os
from .opjects import *

class compFrame():
    
    def __init__(self, parent, components) -> None:
        self.frame = tk.Frame(parent, width=50, height=50, bg="red")
        self.frame.pack()

        self.components = components
        components.append(self)
    
        self.but = Button(self.frame)
        self.but.shape = [50, 50]
        self.but.bg_image = 'GUI_Application/resource/del.jpg'
        self.but.config(command=self.destroy)
        self.but.pack()

        self._com_type = 'R'
        self._n1 = 0
        self._n2 = 0
        self._index = 1
        self._value = 0
        pass

    @property
    def com_type(self):
        return self._com_type
    @com_type.setter
    def com_type(self, val):
        self._com_type = val

    @property
    def index(self):
        return self._index
    @index.setter
    def index(self, val):
        self._index = val
 
    @property
    def n1(self):
        return self._n1
    @n1.setter
    def n1(self, val):
        self._n1 = val
  
    @property
    def n2(self):
        return self._n2
    @n2.setter
    def n2(self, val):
        self._n2 = val

    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, val):
        self._value = val

    def destroy(self):
        self.components.remove(self)
        self.frame.destroy()

    def build_from_str(self, str):
        net = parse(str)
        if len(net) < 4:
            print('Too low argument')
            return

        self.com_type = net[0][0]
        self.index = net[0][1:]
        self.n1 = net[1]
        self.n2 = net[2]
        self.value = net[3]

    def __str__(self) -> str:
        return f'{self.com_type}{self.index} {self.n1} {self.n2} {self.value}'
    
def parse(arg=""):
	return arg.split()
