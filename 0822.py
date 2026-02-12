from tkinter import *

window = Tk()

# ----------Page----------
window.title("Coding Game")
window.config(bg="black")
window.geometry("800x600")
window.resizable(0, 0)


btn1 = Button(window, text="1", width=10, height=5)
btn2 = Button(window, text="2", width=10, height=5)
btn3 = Button(window, text="3", width=10, height=5)
btn4 = Button(window, text="4", width=10, height=5)
btn5 = Button(window, text="5", width=10, height=5)
btn6 = Button(window, text="6", width=10, height=5)

btn1.pack(side=LEFT); btn2.pack(side=LEFT); btn3.pack(side=RIGHT); btn4.pack(side=RIGHT); btn5.pack(side=LEFT); btn6.pack(side=RIGHT)


window.mainloop()