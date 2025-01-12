from turtle import Screen;
import time;
from snake import Snake;


screen = Screen();
screen.bgcolor('black');
screen.setup(width=600, height=600);
screen.tracer(0);
screen.listen();

#Creating snake.
snake = Snake();

screen.onkey(key='Up', fun=snake.MoveUp);
screen.onkey(key='Left', fun=snake.MoveLeft);
screen.onkey(key='Down', fun=snake.MoveDown);
screen.onkey(key='Right', fun=snake.MoveRight);


is_game_on = True;

while is_game_on:
    screen.update();
    time.sleep(0.2);
    snake.move();




screen.exitonclick();