import tkinter as tk
from PIL import Image, ImageTk

from .helper import getImg

class Button(tk.Button):
    
    bg_color = "blue"
    hover_color = "#000000"

    shape = [150, 150]

    def init(self, text="", image=None, command=None):
        self.bind("<Enter>", lambda event:self.hover())
        self.bind("<Leave>", lambda event:self.intial())

        
        self._text = text
        self._bg_image = image
        self._command = command
        self._activebackground = None

        self.config(text=self.text, image=self.bg_image, command=self.command)
        self.intial()

    @property
    def text(self):
        return self._text
    @text.setter
    def text(self, new_text):
        self._text = new_text
        self.config(text=self.text)

    @property
    def activebackground(self):
        return self._activebackground
    @activebackground.setter
    def activebackground(self, new):
        self._activebackground = new
        self.config(activebackground=self.activebackground)

    @property
    def bg_image(self):
        return self._bg_image

    @bg_image.setter
    def bg_image(self, path):
        if not path:
            return
        self._bg_image = getImg(path, self.shape)
        self.configure(image=self.bg_image)

    @property
    def command(self):
        return self._command
    @command.setter
    def command(self, command):
        self._command = command
        self.config(command=self.command)

    def bgColor(self, color):
        self.config(bg=color)

    def intial(self):
        self.bgColor(self.bg_color)

    def hover(self):
        self.bgColor(self.hover_color)
