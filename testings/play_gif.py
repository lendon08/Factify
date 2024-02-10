import tkinter as tk
import time
from PIL import Image, ImageTk


class MyApp(tk.Frame):
    def __init__(self, root):
        super().__init__(root,bg="WHITE")

        self.main_frame = self
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=1)
        
        self.create_widgets
        
    def create_widgets(self):
        self.label_gif1 = tk.Label(
            self.main_frame,
            bg="WHITE",
            border=0,
            highlightthickness=0
        )

        self.label_gif1.grid(column=0, row=0)

        self.button = tk.Button(
            self.main_frame,
            text="Button",
            width=10,
            height=2
        )

        self.button.grid(column=0, row=1)

root = tk.Tk()
root.title("My App")
root.geometry('600x600')
root.resizable(0,0)

my_app_instance = MyApp(root)
root.mainloop()