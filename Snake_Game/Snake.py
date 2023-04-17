import turtle as t


class Snake:

    segments = []
    startingPosition = [(0, 0), (-20, 0), (-40, 0)]

    for position in startingPosition:
        new_segment = t.Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        segments.append(new_segment)

    @staticmethod
    def move():
        """Method that moves all parts of the Snake forward"""

        for seg_num in range(len(Snake.segments) - 1, 0, -1):
            Snake.segments[seg_num].goto(Snake.segments[seg_num - 1].pos())
        Snake.segments[0].forward(20)

    @staticmethod
    def up():
        if Snake.segments[0].heading() != 270:
            Snake.segments[0].setheading(90)

    @staticmethod
    def down():
        if Snake.segments[0].heading() != 90:
            Snake.segments[0].setheading(270)

    @staticmethod
    def left():
        if Snake.segments[0].heading() != 0:
            Snake.segments[0].setheading(180)

    @staticmethod
    def right():
        if Snake.segments[0].heading() != 180:
            Snake.segments[0].setheading(0)

    @staticmethod
    def growSnake():

        new_segment = t.Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto((Snake.segments[-1].xcor()-20, Snake.segments[-1].ycor()))
        Snake.segments.append(new_segment)




