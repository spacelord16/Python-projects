from tkinter import *
from PIL import Image, ImageTk


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        load = Image.open("images (1).jfif")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.imgage = render
        img.place(x=0, y=0)


root = Tk()
app = Window(root)
root.wm_title("Tkinterwindow")
root.geometry("200x120")
root.mainloop()
