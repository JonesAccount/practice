from tkinter import *

window = Tk()

# ----------Page----------
window.title("Program")
window.config(bg="black")
window.geometry("800x600")
window.resizable(0, 0)

frm = Frame(window)
frm.pack(fill=BOTH, expand=1)

# ----------Function----------
def page2():
    frm.config(bg="green")
    btn2.pack(expand=1)
    btn1.pack_forget()

def page1():
    frm.config(bg="red")
    btn1.pack(expand=1)
    btn2.pack_forget()

# ----------Button----------
btn1 = Button(frm, text="1 page", font="Arial 40")
btn2 = Button(frm, text="2 page", font="Arial 40")
btn1.config(command=page2)
btn2.config(command=page1)

page1()

window.mainloop()