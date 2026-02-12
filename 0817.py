from tkinter import *

window = Tk()

# ----------Page----------
window.title("Coding Game")
window.config(bg="black")
window.geometry("800x600")
window.resizable(0, 0)

frm1 = Frame(master=window, width=250, height=250, background="red")
frm2 = Frame(master=window, width=200, height=200, background="yellow")
frm3 = Frame(master=window, width=150, height=150, background="blue")

frm1.pack(); frm2.pack(); frm3.pack()

window.mainloop()