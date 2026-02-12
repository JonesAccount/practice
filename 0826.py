from tkinter import *

window = Tk()

# ----------Page----------
window.title("Coding Game")
window.config(bg="black")
window.geometry("800x600")
window.resizable(0, 0)


frm1 = Frame(master=window, width=50, height=50, bg="red")
frm2 = Frame(master=window, width=50, height=50, bg="red")
frm3 = Frame(master=window, width=50, height=50, bg="red")
frm4 = Frame(master=window, width=50, height=50, bg="red")
frm5 = Frame(master=window, width=50, height=50, bg="red")

frm1.pack(side=TOP)
frm2.pack(side=BOTTOM)
frm3.pack(side=LEFT)
frm4.pack(side=RIGHT)
frm5.pack(side=LEFT, expand=True)



window.mainloop()