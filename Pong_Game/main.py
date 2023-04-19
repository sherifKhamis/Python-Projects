# Basic Pong Game using the turtle library

from paddle import Paddle
from ball import Ball
import turtle as t
import random
from scoreboard import Scoreboard

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
scoreboard = Scoreboard()

window.listen()
window.onkey(Paddle.l_Up, "w")
window.onkey(Paddle.l_Down, "s")
window.onkey(Paddle.r_Up, "Up")
window.onkey(Paddle.r_Down, "Down")

ball = Ball()

# Start Game
ball.speed(1)
ball.goto(random.choice([-365, 360]), random.randint(-280, 280))


def collision():

    if ball.distance(paddles.left_paddle.pos()) < 50:
        if ball.speed() < 5:
            ball.speed(ball.speed()+0.5)
        ball.goto(360, random.randint(-280, 280))
        return

    if ball.distance(paddles.right_paddle.pos()) < 50:
        if ball.speed() < 5:
            ball.speed(ball.speed() + 0.5)
        ball.goto(-365, random.randint(-280, 280))
        return

    if -365 == ball.xcor():
        scoreboard.increase_r_score()
        ball.resetBallPos()
        return

    if 360 == ball.xcor():
        scoreboard.increase_l_score()
        ball.resetBallPos()
        return


game_running = True
while game_running:

    collision()

window.exitonclick()




