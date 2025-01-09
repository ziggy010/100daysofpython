from turtle import Turtle, Screen;

screen = Screen();

screen.bgcolor('black');
screen.setup(width=600, height=600);
screen.title("My snake game!");


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
    for item in snakes:
        item.forward(20);





















screen.exitonclick();