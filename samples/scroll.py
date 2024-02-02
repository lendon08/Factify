#import modules
 

import tkinter.messagebox
import customtkinter
from customtkinter import *
import os
 
# Designing window for registration
 

class MyFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.radiobuttons = []
        # add widgets onto the frame...
        self.label = customtkinter.CTkLabel(self)
        self.label.grid(row=0, column=0, padx=20)
        for i in range(30):
            self.logo_label = customtkinter.CTkLabel(self, height=48, width=280, text="Factify")
            self.logo_label.grid(row=i + 1, column=0, padx=20, pady=(20, 10))


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.my_frame = MyFrame(master=self, width=300, height=200)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20)


app = App()
app.mainloop()