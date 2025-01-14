from turtle import Screen;
import time;
from snake import Snake;
from food import Food;
from scoreboard import ScoreBoard;


screen = Screen();
screen.bgcolor('black');
screen.setup(width=600, height=600);
screen.tracer(0);
screen.listen();

#Creating snake.
snake = Snake();

#Creating food
food = Food();

#creating scoreboard
scoreboard = ScoreBoard();

screen.onkey(key='Up', fun=snake.MoveUp);
screen.onkey(key='Left', fun=snake.MoveLeft);
screen.onkey(key='Down', fun=snake.MoveDown);
screen.onkey(key='Right', fun=snake.MoveRight);


is_game_on = True;

while is_game_on:
    screen.update();
    time.sleep(0.1);
    snake.move();

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.new_food();
        scoreboard.add_score();
        snake.extend();

    #detech collision with wall.abs
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False;
        scoreboard.game_over();
    
    #detect collision with tail
    for item in snake.snake_segments[1:]:
        if snake.head.distance(item) < 15:
            is_game_on = False;
            scoreboard.game_over();



screen.exitonclick();