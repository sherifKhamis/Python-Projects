from player import Player
from cars import Cars
import turtle as t
import random
import time
from scoreboard import Scoreboard

window = t.Screen()
window.screensize(600, 600)
window.tracer(0)

player = Player()
scoreboard = Scoreboard()

window.listen()
window.onkey(player.move_forward, "Up")
window.onkey(player.move_backwards, "Down")

starting_cars = 15
all_cars = []
for i in range(starting_cars):
    new_car = Cars()
    all_cars.append(new_car)

game_is_on = True
while game_is_on:

    time.sleep(0.1)
    for i in range(starting_cars//2):

        all_cars[random.randint(0, starting_cars-1)].move()
        window.update()

    for i in range(starting_cars):
        if player.distance(all_cars[i]) < 35:
            window.update()
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() > 400:
        scoreboard.increase_level()
        starting_cars += 3
        all_cars = []
        for i in range(starting_cars):
            new_car = Cars()
            all_cars.append(new_car)

        player.hideturtle()
        player.goto(0, -350)
        player.showturtle()


window.exitonclick()
