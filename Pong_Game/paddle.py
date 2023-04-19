import turtle as t


class Paddle:

    left_paddle = t.Turtle()
    left_paddle.hideturtle()
    left_paddle.color("white")
    left_paddle.shape("square")
    left_paddle.shapesize(stretch_wid=5, stretch_len=1)
    left_paddle.speed("fastest")
    left_paddle.penup()
    left_paddle.goto(-380, 0)
    left_paddle.showturtle()

    right_paddle = t.Turtle()
    right_paddle.hideturtle()
    right_paddle.color("white")
    right_paddle.shape("square")
    right_paddle.shapesize(stretch_wid=5, stretch_len=1)
    right_paddle.speed("fastest")
    right_paddle.penup()
    right_paddle.goto(370, 0)
    right_paddle.showturtle()


