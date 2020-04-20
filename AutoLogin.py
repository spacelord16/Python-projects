from selenium import webdriver
from tkinter import *
import tkinter.ttk as ttk
import time
from tkinter.messagebox import showinfo

win = Tk()

win.title("Instagram Login")
win.geometry("250x100")

def automatic():
    username_automation = username.get()
    password_automation = password.get()

    if username_automation == "" or password_automation == "" :
        showinfo("Instagram Login", "Please Add Username and Password")
    else:
        driver = webdriver.Chrome()
        