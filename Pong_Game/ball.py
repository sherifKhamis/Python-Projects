from turtle import Turtle as t
import random


class Ball(t):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.resetBallPos()

    def resetBallPos(self):
        self.hideturtle()
        self.speed("fastest")
        self.goto(0, random.randint(-300, 300))
        self.showturtle()
        self.speed(1)
        self.goto(random.choice([-365, 360]), random.randint(-280, 280))

