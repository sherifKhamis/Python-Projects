from turtle import Turtle as t


class Scoreboard(t):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.pencolor("black")
        self.goto(-410, 390)
        self.write("Level = " + str(self.level), font=("Arial", 15, "normal"))

    def game_over(self):
        self.penup()
        self.goto(-120, 0)
        self.write("GAME OVER", font=("Arial", 30, "normal"))

    def increase_level(self):
        self.level += 1
        self.penup()
        self.clear()
        self.goto(-410, 390)
        self.write("Level = " + str(self.level), font=("Arial", 15, "normal"))



