from tkinter import *

window = Tk()

# ----------Page----------
window.title("Coding Game")
window.config(bg="black")
window.geometry("800x600")
window.resizable(0, 0)


frm1 = Frame(window, width=200, bg="blue")
frm2 = Frame(window, width=200, bg="red")
frm3 = Frame(window, width=200, bg="green")
frm4 = Frame(window, height=100, bg="yellow")

frm1.pack(fill=Y, side=LEFT)
frm2.pack(fill=Y, side=RIGHT)
frm3.pack(fill=Y, side=LEFT)
frm4.pack(fill=X, side=LEFT)


window.mainloop()