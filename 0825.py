from tkinter import *
from time import sleep

window = Tk()

# ----------Page----------
window.title("Coding Game")
window.config(bg="black")
window.geometry("800x600")
window.resizable(1, 1)

frm1 = Frame(window, width=200, bg="red")
frm2 = Frame(window, width=200, bg="yellow")
frm3 = Frame(window, width=200, bg="green")

frm1.pack(fill=Y, side=LEFT, expand=False)
frm2.pack(fill=Y, side=LEFT, expand=True)
frm3.pack(fill=Y, side=RIGHT, expand=False)

window.mainloop()