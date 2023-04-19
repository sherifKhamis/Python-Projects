# Basic Pong Game using the turtle library

import turtle as t
from paddle import *

window = t.Screen()
window.bgcolor("black")
window.setup(800, 600)
window.title("Pong Game")

middle_line = t.Turtle()
middle_line.hideturtle()
middle_line.pencolor("white")
middle_line.penup()
middle_line.speed("fastest")
middle_line.goto(0, 300)
while middle_line.pos() != (0, -300):
    middle_line.pendown()
    middle_line.goto(0, middle_line.ycor()-15)
    middle_line.penup()
    middle_line.goto(0, middle_line.ycor()-15)

paddles = Paddle()

window.exitonclick()



