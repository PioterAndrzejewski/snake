
from turtle import Turtle

STARTING_COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
RIGHT = 0
DOWN = 270
LEFT = 180


class Snake:
    def __init__(self):
        self.starting_position = STARTING_COORDINATES
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in self.starting_position:
            segment = Turtle(shape="square")
            segment.penup()
            segment.color("white")
            segment.shapesize(stretch_len=0.9, stretch_wid=0.9)
            segment.goto(position)
            self.segments.append(segment)

    def add_segment(self):
        segment = Turtle(shape="square")
        segment.penup()
        segment.color("white")
        new_x = self.segments[len(self.segments)-1].xcor()
        new_y = self.segments[len(self.segments)-1].ycor()
        segment.shapesize(stretch_len=0.9, stretch_wid=0.9)
        segment.goto((new_x, new_y))
        self.segments.append(segment)

    def move_up(self):
        if not self.segments[0].heading() == DOWN:
            self.segments[0].setheading(UP)

    def move_down(self):
        if not self.segments[0].heading() == UP:
            self.segments[0].setheading(DOWN)

    def move_right(self):
        if not self.segments[0].heading() == LEFT:
            self.segments[0].setheading(RIGHT)

    def move_left(self):
        if not self.segments[0].heading() == RIGHT:
            self.segments[0].setheading(LEFT)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto((new_x, new_y))
        self.segments[0].forward(MOVE_DISTANCE)
