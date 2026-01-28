import turtle, time
joe = turtle.Turtle()
window = turtle.Screen()
joe.hideturtle()
window.bgcolor("orange")
joe.color("black")
joe.speed(10)
joe.up()
joe.setposition(-100, 0)
joe.down()

joe.begin_fill()
for i in range(3):
    joe.fd(200)
    joe.left(120)
joe.end_fill()

time.sleep(5)

# begin_fill() и end_fill() обозначают начало и конец заполнения/заливки объекта цветом.
