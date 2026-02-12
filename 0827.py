from tkinter import *

window = Tk()

# ----------Page----------
window.title("Coding Game")
window.config(bg="black")
window.geometry("800x800")
window.resizable(1, 1)

frm1 = Frame(window, width=200, height=200, bg="red")
frm2 = Frame(window, width=200, height=200, bg="green")
frm3 = Frame(window, width=200, height=200, bg="purple")
frm4 = Frame(window, width=200, height=200, bg="blue")
frm5 = Frame(window, width=200, height=200, bg="brown")
frm6 = Frame(window, width=200, height=200, bg="yellow")
frm7 = Frame(window, width=200, height=200, bg="orange")
frm8 = Frame(window, width=200, height=200, bg="lime")
frm9 = Frame(window, width=200, height=200, bg="gray")

frm1.place(x=0)
frm2.place(x=300)
frm3.place(x=600)

frm4.place(y=300)
frm5.place(x=300, y=300)
frm6.place(x=600, y=300)

frm7.place(y=600)
frm8.place(x=300, y=600)
frm9.place(x=600, y=600)a

window.mainloop()