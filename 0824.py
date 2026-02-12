from tkinter import *
from time import sleep

window = Tk()

# ----------Page----------
window.title("Coding Game")
window.config(bg="black")
window.geometry("800x600")
window.resizable(0, 0)

frm1 = Frame(window, width=200, bg="red")
frm2 = Frame(window, width=200, bg="yellow")
frm3 = Frame(window, width=200, bg="green")
frm4 = Frame(window, width=200, bg="blue")
frm5 = Frame(window, width=200, bg="purple")

lst = [frm1, frm2, frm3, frm4, frm5]

for i in range(5):
    lst[i].pack(fill=Y, side=LEFT)
    sleep(2)

window.mainloop()