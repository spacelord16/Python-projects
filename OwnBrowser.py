import tkinter as tk
from tkinter import *
import webbrowser


def google():
    webbrowser.open("")


def facebook():
    webbrowser.open("")


igoogle = PhotoImage(file="")
google = tk.button(win, image=igoogle, command=google)
google.grid(row=0, column=0)

iyoutube = PhotoImage(file="")
youtube = tk.button(win, image=iyoutube, command=youtube)
youtube.grid(row=0, column=1)
