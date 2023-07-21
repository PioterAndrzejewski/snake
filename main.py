import time
from turtle import Screen
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_right, "Right")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_down, "Down")
screen.listen()

game_is_on = True

while game_is_on:
    time.sleep(0.075)
    screen.update()
    snake.move()

    if snake.head.distance(food) < 15:
        food.collided()
        score.add_point()
        snake.add_segment()

    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        game_is_on = False
        score.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()


screen.exitonclick()