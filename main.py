from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

starting_position = [(0,0), (-20, 0), (-40, 0)]

segments = []

for position in starting_position:
    segment = Turtle(shape="square")
    segment.penup()
    segment.color("white")
    segment.goto(position)
    segments.append(segment)

screen.update()

game_is_on = True

while game_is_on:
    time.sleep(0.3)
    screen.update()
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)

screen.exitonclick()