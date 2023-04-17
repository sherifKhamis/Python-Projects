from turtle import Turtle as t


class Scoreboard(t):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 380)
        self.refreshBoard()

    def increaseScore(self):
        self.score += 1
        self.clear()
        self.refreshBoard()

    def refreshBoard(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 20, "normal"))

    def gameOver(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 40, "normal"))
