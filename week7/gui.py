from tkinter import *

class Gui(Tk):
    def __init__(self):
        super().__init__()

        self.geometry("500x500")
        self.title("Trip_sample")

        #changing in the ICON
        p1=PhotoImage(file="C:\Users\0bandn32\PycharmProjects\com714\week7\download.png")
        self.iconphoto(False, PhotoImage(p1))

if __name__ == '__main__':
        app = Gui()
        app.mainloop()
