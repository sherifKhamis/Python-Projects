from turtle import Turtle as t
import random
from turtle import Screen


class Cars(t):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(1, 3)
        self.hideturtle()
        self.speed(0)
        self.goto(random.randint(150, 300), random.randint(-250, 250))
        Screen().colormode(255)
        self.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.showturtle()

    def move(self):

        if self.xcor() < -400:
            self.hideturtle()
            self.speed(0)
            self.goto(random.randint(150, 400), random.randint(-250, 250))
            self.showturtle()

        self.speed(random.choice([1, 3, 6]))
        self.goto(self.xcor() - 20, self.ycor())


