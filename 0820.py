from tkinter import *

window = Tk()

# ----------Page----------
window.title("Coding Game")
window.config(bg="black")
window.geometry("800x600")
window.resizable(1, 1)

frm1 = Frame(master=window,  height=100, background="red")
frm2 = Frame(master=window,  height=100, background="yellow")
frm3 = Frame(master=window,  height=100, background="purple")
frm4 = Frame(master=window,  height=100, background="blue")
frm5 = Frame(master=window,  height=100, background="green")
frm6 = Frame(master=window,  height=100, background="green")

lst = [frm1, frm2, frm3, frm4, frm5, frm6]

for i in range(5):
    lst[i].pack(fill=BOTH)

window.mainloop()