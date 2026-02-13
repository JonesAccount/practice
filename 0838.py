from tkinter import *

window = Tk()

# ----------Page----------
window.title("Program")
window.config(bg="black")
window.geometry("600x400")
window.resizable(0, 0)


# ----------Variable----------
counter1 = 0
counter2 = 0

# ----------Function----------
def timer1():
    global counter1
    counter1 += 1
    lbl1.config(text=counter1)
    window.after(1000, timer1)

def play_time1(event):
    timer1()

def timer2():
    global counter2
    counter2 += 1
    lbl2.config(text=counter2)
    window.after(100, timer2)

def play_time2(event):
    timer2()

# ----------Frame----------


# ----------Label----------
lbl1 = Label(master=window, text=counter1, font="Arial 100 bold", bg="black", fg="white")
lbl2 = Label(master=window, text=counter2, font="Arial 100 bold", bg="black", fg="white")


# ----------Entry----------


# ----------Text----------


# ----------Button----------
btn1 = Button(master=window, text=" ", bg="white", fg="black", width=5, height=5)
btn2 = Button(master=window, text=" ", bg="white", fg="black", width=5, height=5)


# ----------Event----------
btn1.bind("<Button-1>", play_time1)
btn2.bind("<Button-1>", play_time2)


# ----------Show widget----------
lbl1.place(x=130, y=70)
lbl2.place(x=400, y=70)

btn1.place(x=120, y=200)
btn2.place(x=390, y=200)


window.mainloop()