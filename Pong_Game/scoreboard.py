from turtle import Turtle as t


class Scoreboard(t):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.pencolor("white")
        self.goto(-150, 200)
        self.write(self.l_score, font=("Arial", 50, "normal"))
        self.goto(130, 200)
        self.write(self.r_score, font=("Arial", 50, "normal"))

    def increase_l_score(self):

        self.l_score += 1
        self.clear()
        self.goto(-150, 200)
        self.write(self.l_score, font=("Arial", 50, "normal"))
        self.goto(130, 200)
        self.write(self.r_score, font=("Arial", 50, "normal"))

    def increase_r_score(self):
        self.r_score += 1
        self.clear()
        self.goto(-150, 200)
        self.write(self.l_score, font=("Arial", 50, "normal"))
        self.goto(130, 200)
        self.write(self.r_score, font=("Arial", 50, "normal"))
