import pandas as pd
import turtle

window = turtle.Screen()
window.title("Germany 16 States Game")
# Screensize = (400, 300)

image = "16_states.gif"
window.addshape(image)
turtle.shape(image)

data = pd.read_csv("16_states.csv")
state_name = window.textinput("", "Guess a state name: ")

game_is_on = True
while game_is_on:
    window.exitonclick()
    for name in data["bundesländer"]:
        if name == state_name:
            new_state = turtle.Turtle()
            new_state.penup()
            new_state.hideturtle()
            state_data = data[data.bundesländer == name]
            new_state.goto(int(state_data.x), int(state_data.y))
            new_state.write(name, align="center", font=("Arial", 10, "normal"))
    state_name = window.textinput("", "Guess another state name: ")

