import tkinter as tk

win = tk.Tk()
win.title("Radio Button")

var = tk.IntVar

value_1 = tk.Radiobutton(win, text="India", value=1, variable=var).pack()
value_2 = tk.Radiobutton(win, text="USA", value=2, variable=var).pack()
value_3 = tk.Radiobutton(win, text="UK", value=3, variable=var).pack()

win.mainloop()
