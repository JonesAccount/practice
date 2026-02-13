from tkinter import *

window = Tk()

# ----------Page----------
window.title("Program")
window.config(bg="pink")
window.geometry("800x600")
window.resizable(0, 0)


# ----------Variable----------


# ----------Function----------
def enter(event):
    ent.delete(0, END)
    ent.insert(END, "Навел")

def leave(event):
    ent.delete(0, END)
    ent.insert(END, "Не навел")


# ----------Frame----------


# ----------Label----------


# ----------Entry----------
ent = Entry(master=window, font=("Arial", 50), width=50, bg="purple", fg="white")
ent.insert(0, "Не навел")


# ----------Text----------


# ----------Button----------
btn = Button(master=window, text="", width=10, height=7, bg="purple", fg="white")


# ----------Event----------
btn.bind("<Enter>", enter)
btn.bind("<Leave>", leave)


# ----------Show widget----------
ent.grid(row=0, column=0)
btn.place(relx=0.5, rely=0.5, anchor="center")


window.mainloop()