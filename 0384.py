import turtle

figure = turtle.Turtle()
figure.speed(5)

figure.up()
figure.setposition(+50, -450)
figure.down()

def hexagon(angle, length):
    n_angle = 360 / angle
    for i in range(angle):
        figure.forward(length)
        figure.left(n_angle)
    
hexagon(6, 150)