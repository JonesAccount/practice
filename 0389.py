import turtle
joe = turtle.Turtle()
window = turtle.Screen()

colors = ["white", "black"]
joe.hideturtle()

def block():
    for i in range(1000):
        window.bgcolor(colors[i % 2])
        
def move(x, y):
    block()

window.onclick(move)
window.listen()
window.mainloop()

# bgcolor() устанавливает цвет фона холста.