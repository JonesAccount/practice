from tkinter import *

window = Tk()

# ----------Page----------
window.title("Coding Game")
window.config(bg="black")
window.geometry("800x600")
window.resizable(0, 0)

frm1 = Frame(master=window, width=150, height=150, background="red")
frm2 = Frame(master=window, width=100, height=100, background="yellow")
frm3 = Frame(master=window, width=50, height=50, background="purple")
frm4 = Frame(master=window, width=100, height=100, background="blue")
frm5 = Frame(master=window, width=150, height=150, background="green")

frm1.pack(); frm2.pack(); frm3.pack(); frm4.pack(); frm5.pack()

window.mainloop()