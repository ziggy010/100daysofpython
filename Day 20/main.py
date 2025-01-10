from turtle import Turtle, Screen;
import time;

screen = Screen();

screen.bgcolor('black');
screen.setup(width=600, height=600);
screen.title("My snake game!");
screen.tracer(0);


starting_position = [(0,0), (-20, 0), (-40, 0)];

snakes = [];

for i in starting_position:
    snake = Turtle(shape="square");
    snake.penup();
    snake.color('white');
    snake.goto(i)
    snakes.append(snake);


is_game_on = True;

while is_game_on:
    screen.update();
    time.sleep(0.2);
    for item in range(len(snakes)-1,0,-1):
        x_cor = snakes[item - 1].xcor();
        y_cor = snakes[item - 1].ycor();
        snakes[item].goto(x_cor, y_cor);
    

























screen.exitonclick();