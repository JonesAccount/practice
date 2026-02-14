from tkinter import *

window = Tk()

# ----------Page----------
window.title("Program")
window.config(bg="black")
window.geometry("800x600")
window.resizable(0, 0)


# ----------Variable----------


# ----------Function----------
def func_e(event):
    btn.pack_forget()
    
def func_l(event):
    btn.pack(expand=True, anchor=CENTER)


# ----------Frame----------


# ----------Label----------


# ----------Entry----------


# ----------Text----------


# ----------Button----------
btn = Button(master=window, text="Click Me!", font=("Segoe UI", 20, "bold"), bg="black", fg="white")


# ----------Event----------
btn.bind("<Enter>", func_e)
btn.bind("<Leave>", func_l)


# ----------Show widget----------
btn.pack(expand=True, anchor=CENTER)


window.mainloop()