import turtle
import time


def draw():
    colors = ['red', 'green', 'blue', 'magenta', 'cyan', 'white']
    turtle.pensize(5)
    turtle.bgcolor('black')
    turtle.speed(1000)

    for x in range(360):
        turtle.pencolor(colors[x % len(colors)])
        turtle.pensize(x/50)
        turtle.forward(x)
        turtle.left(59)

draw()
time.sleep(5)
