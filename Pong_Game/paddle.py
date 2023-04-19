import turtle as t


class Paddle:

    left_paddle = t.Turtle()
    left_paddle.hideturtle()
    left_paddle.color("white")
    left_paddle.shape("square")
    left_paddle.shapesize(stretch_wid=5, stretch_len=1)
    left_paddle.speed("fastest")
    left_paddle.penup()
    left_paddle.goto(-360, 0)
    left_paddle.showturtle()

    right_paddle = t.Turtle()
    right_paddle.hideturtle()
    right_paddle.color("white")
    right_paddle.shape("square")
    right_paddle.shapesize(stretch_wid=5, stretch_len=1)
    right_paddle.speed("fastest")
    right_paddle.penup()
    right_paddle.goto(360, 0)
    right_paddle.showturtle()

    @staticmethod
    def l_Up():
        if Paddle.left_paddle.ycor() < 230:
            Paddle.left_paddle.goto(Paddle.left_paddle.xcor(), Paddle.left_paddle.ycor() + 50)

    @staticmethod
    def l_Down():
        if Paddle.left_paddle.ycor() > -230:
            Paddle.left_paddle.goto(Paddle.left_paddle.xcor(), Paddle.left_paddle.ycor() - 50)

    @staticmethod
    def r_Up():
        if Paddle.right_paddle.ycor() < 230:
            Paddle.right_paddle.goto(Paddle.right_paddle.xcor(), Paddle.right_paddle.ycor() + 50)

    @staticmethod
    def r_Down():
        if Paddle.right_paddle.ycor() > -230:
            Paddle.right_paddle.goto(Paddle.right_paddle.xcor(), Paddle.right_paddle.ycor() - 50)
