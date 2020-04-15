import tkinter as tk
from tkhtmlview import HTMLLabel

win = tk.Tk()
win.title("Link in Tkinter")

instagram = HTMLLabel(win, html='<a href ="www.instagram.com"> Instagram </a>')
google = HTMLLabel(win, html='<a href = "www.google.co.in"> Google </a>')
whatsapp = HTMLLabel(win, html='<a href ="web.whatsapp.com"> Whatsapp </a>')
News = HTMLLabel(win, html='<a href ="news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en"> News </a>')
instagram.grid(row=0,column=0)
google.grid(row=0,column=1)
whatsapp.grid(row=0,column=2)
News.grid(row=1,column=0)

win.mainloop()
