import tkinter as tk
import customtkinter
from customtkinter import *
from PIL import Image, ImageTk
from itertools import count
import os

class LoadingLabel(customtkinter.CTkLabel):
    """a label that displays images, and plays them if they are gifs"""

    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(self.frames) == 1:
            self.configure(image=self.frames[0])
        else:
            self.next_frame()

    def unload(self):
        self.config(image="")
        self.frames = None

    def next_frame(self):
        self.update()
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.configure(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)

root = tk.Tk()

lbl = LoadingLabel(root, text="")

lbl.pack()
loading_img_data = Image.open(os.path.join('images', "loading.gif"), 'r')
loading_img = CTkImage(dark_image=loading_img_data, light_image=loading_img_data)

lbl.load(loading_img_data)

root.mainloop()