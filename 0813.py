from tkinter import *

window = Tk()

window.title("My first GUI")
window.config(background="gray")
window.iconbitmap("g.jpg")

window.geometry("500x500")
window.resizable(1, 0)

fr1 = Frame(); fr2 = Frame()
fr1.pack(); fr2.pack()

label1 = Label(master=fr1, text="This is text"); label2 = Label(master=fr2, text="This is string")
label1.pack(); label2.pack()

fr1.pack(); fr2.pack()



window.mainloop()