from tkinter import *

class Gui(Tk):
    def __init__(self):
        super().__init__()

        # set window attributes
        self.title("The Life Project")
        self.configure(padx=10, pady=10)

        # add components
        self.__add_heading_label()
        # ...other components here

    def __add_heading_label(self):
        # create
        self.heading_label = Label()
        # layout
        self.heading_label.grid(row=0, column=0)
        # style
        self.heading_label.configure(font="Arial 24",text="The Life Project")