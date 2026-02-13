from tkinter import *

window = Tk()

# ----------Page----------
window.title("Program")
window.config(bg="black")
window.geometry("800x800")
window.resizable(0, 0)


# ----------Variable----------


# ----------Function----------


# ----------Frame----------
frm1 = Frame(window, bg="white", width=100, height=100)
frm2 = Frame(window, bg="white", width=100, height=100)
frm3 = Frame(window, bg="white", width=100, height=100)
frm4 = Frame(window, bg="white", width=100, height=100)
frm5 = Frame(window, bg="white", width=100, height=100)
frm6 = Frame(window, bg="white", width=100, height=100)
frm7 = Frame(window, bg="white", width=100, height=100)
frm8 = Frame(window, bg="white", width=100, height=100)
frm9 = Frame(window, bg="white", width=100, height=100)
frm10 = Frame(window, bg="white", width=100, height=100)
frm11 = Frame(window, bg="white", width=100, height=100)
frm12 = Frame(window, bg="white", width=100, height=100)
frm13 = Frame(window, bg="white", width=100, height=100)
frm14 = Frame(window, bg="white", width=100, height=100)
frm15 = Frame(window, bg="white", width=100, height=100)
frm16 = Frame(window, bg="white", width=100, height=100)
frm17 = Frame(window, bg="white", width=100, height=100)

# ----------Label----------


# ----------Entry----------


# ----------Text----------


# ----------Button----------


# ----------Show widget----------
frm1.grid(row=0, column=0, padx=50, pady=50); frm2.grid(row=0, column=1, pady=50); frm3.grid(row=0, column=2, padx=50, pady=50); frm4.grid(row=0, column=3, pady=50); frm5.grid(row=0, column=4, padx=50, pady=50)
frm6.grid(row=1, column=0); frm7.grid(row=1, column=4)
frm8.grid(row=2, column=0, pady=50); frm17.grid(row=2, column=2); frm9.grid(row=2, column=4)
frm10.grid(row=3, column=0); frm11.grid(row=3, column=4)
frm12.grid(row=4, column=0, padx=50, pady=50); frm13.grid(row=4, column=1, pady=50); frm14.grid(row=4, column=2, padx=50, pady=50); frm15.grid(row=4, column=3, pady=50); frm16.grid(row=4, column=4, padx=50, pady=50)



window.mainloop()