
from turtle import Turtle

STARTING_COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.starting_position = STARTING_COORDINATES
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in self.starting_position:
            segment = Turtle(shape="square")
            segment.penup()
            segment.color("white")
            segment.goto(position)
            self.segments.append(segment)

    def move_up(self):
        if not self.segments[0].heading() == 270:
            self.segments[0].setheading(90)

    def move_down(self):
        if not self.segments[0].heading() == 90:
            self.segments[0].setheading(270)

    def move_right(self):
        if not self.segments[0].heading() == 180:
            self.segments[0].setheading(0)

    def move_left(self):
        if not self.segments[0].heading() == 0:
            self.segments[0].setheading(180)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto((new_x, new_y))
        self.segments[0].forward(MOVE_DISTANCE)
