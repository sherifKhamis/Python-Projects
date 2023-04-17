import random
from turtle import Turtle as t


class Food(t):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        self.speed("fastest")
        self.goto(random.randint(-380, 380), random.randint(-380, 380))

    def refresh(self):
        self.goto(random.randint(-380, 380), random.randint(-380, 380))
