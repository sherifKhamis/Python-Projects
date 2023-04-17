# Python project using the turtle library to create a random generated
# hirst painting

import turtle as t
import random

# Make the turtles starting position in the top left
turtle_cursor = t.Turtle(visible=False)
initial_speed = t.speed()
t.speed(0)
t.up()
t.setpos(-400, 400)
t.shape("turtle")
t.color("grey")
t.showturtle()
t.Screen().colormode(255)
t.Screen().bgcolor((222, 209, 180))


def draw_Circles():
    """Function that draws all circles of the painting"""
    t.colormode(255)
    if t.ycor() < -400:
        return
    else:
        if t.pos()[0] <= 400:
            t.dot(15, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            t.fd(30)
            draw_Circles()
        else:
            t.setpos(-400, t.ycor()-40)
            draw_Circles()


draw_Circles()

window = t.Screen()
window.exitonclick()
t.done()
