from turtle import Turtle as t


class Player(t):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed(0)
        self.penup()
        self.goto(0, -300)
        self.setheading(90)
        self.shape("turtle")
        self.turtlesize(1.5, 1.5)
        self.showturtle()

    def move_forward(self):

        self.forward(20)

    def move_backwards(self):

        self.forward(-20)
