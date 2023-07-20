import time
from turtle import Screen, Turtle
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()

screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_right, "Right")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_down, "Down")
screen.listen()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    snake.move()
