from tkinter import *

window = Tk()

window.title("My first GUI")
window.config(background="gray")
window.iconbitmap("g.jpg")

window.geometry("500x500")
window.resizable(1, 0)

frame1 = Frame(master=window, relief=FLAT, borderwidth=5)
frame2 = Frame(master=window, relief=SUNKEN, borderwidth=5)
frame3 = Frame(master=window, relief=RAISED, borderwidth=5)
frame4 = Frame(master=window, relief=GROOVE, borderwidth=5)
frame5 = Frame(master=window, relief=RIDGE, borderwidth=5)
frame1.pack(); frame2.pack(); frame3.pack(); frame4.pack(); frame5.pack()

label1 = Label(master=frame1, text="FLAT")
label2 = Label(master=frame2, text="SUNKEN")
label3 = Label(master=frame3, text="RAISED")
label4 = Label(master=frame4, text="GROOVE")
label5 = Label(master=frame5, text="RIDGE") 
label1.pack(); label2.pack(); label3.pack(); label4.pack(); label5.pack()


window.mainloop()