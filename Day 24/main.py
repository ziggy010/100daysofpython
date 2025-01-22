from turtle import Screen;
from snake import Snake;
import time;
from food import Food;
from scoreboard import ScoreBoard;

screen = Screen();
screen.bgcolor('black');
screen.setup(width=800, height=600);
screen.tracer(0);
screen.listen();

#creating snake
snake = Snake();

#creating food
food = Food();

#creating scoreboard
scoreboard = ScoreBoard();

#listening key press
screen.onkey(key='Up', fun=snake.move_up);
screen.onkey(key='Down', fun=snake.move_down);
screen.onkey(key='Left', fun=snake.move_left);
screen.onkey(key='Right', fun=snake.move_right);

is_game_on = True;


while is_game_on:
    time.sleep(0.15);
    screen.update();

    snake.move();

    if snake.head.distance(food) < 15:
        food.create_food();
        snake.extend_snake();
        scoreboard.update_score();

    if snake.head.xcor() > 390 or snake.head.xcor() < -390 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset();
        snake.reset();

    for item in snake.snake_segment[1:]:
        if snake.head.distance(item) < 5:
            scoreboard.reset();
            snake.reset();





screen.exitonclick();