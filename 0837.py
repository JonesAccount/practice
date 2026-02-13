from tkinter import *

window = Tk()

# ----------Page----------
window.title("Program")
window.config(bg="black")
window.geometry("800x600")
window.resizable(0, 0)


# ----------Variable----------


# ----------Function----------
def func(event):
    btn.config(text=ent.get())


# ----------Frame----------


# ----------Label----------
lbl = Label(window,text="dddddd",font="Arial 20")
lbl.pack()


# ----------Entry----------
ent = Entry(master=window, show="*")
ent.pack()


# ----------Text----------


# ----------Button----------
btn = Button(master=window, text=" ", font="Aral 20", bg="white", fg="blue",)
btn.pack(expand=True, anchor=CENTER)


# ----------Event----------
btn.bind("<Button-1>", func)


# ----------Show widget----------


window.mainloop()