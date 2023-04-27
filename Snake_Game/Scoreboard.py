from turtle import Turtle as t


class Scoreboard(t):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 380)
        database = open("database.txt", "r+")
        self.high_score = int(database.read())
        database.close()
        self.refreshBoard()


    def increaseScore(self):
        self.score += 1
        self.clear()
        self.refreshBoard()

    def refreshBoard(self):
        self.goto(-150, 375)
        self.write(f"Score: {self.score}", font=("Arial", 20, "normal"))

        self.goto(30, 375)
        self.write(f"Highscore: {self.high_score}", font=("Arial", 20, "normal"))

    def gameOver(self):
        if self.high_score < self.score:
            database = open("database.txt", "w")
            database.write(str(self.score))
            database.close()

        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 40, "normal"))
