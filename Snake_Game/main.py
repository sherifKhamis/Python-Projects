# Basic snake game using turtle library
from Snake import *
import time
from food import Food
from Scoreboard import Scoreboard


t.Screen().bgcolor("black")
window = t.Screen()
window.screensize(400, 400)
window.title("Snake Game in Python")
window.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

window.listen()
window.onkey(snake.up, "Up")
window.onkey(snake.down, "Down")
window.onkey(snake.left, "Left")
window.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    window.update()
    time.sleep(0.1)

    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.growSnake()
        scoreboard.increaseScore()

    if snake.segments[0].xcor() > 390 or snake.segments[0].xcor() < -390 or snake.segments[0].ycor() > 390 or snake.segments[0].ycor() < -390:
        scoreboard.gameOver()
        game_is_on = False

    for seg in snake.segments:
        if seg == snake.segments[0]:
            continue
        if snake.segments[0].distance(seg) < 10:
            scoreboard.gameOver()
            game_is_on = False

    snake.move()

window.exitonclick()