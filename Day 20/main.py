from turtle import Screen;
import time;
from Snake import Snake;
from food import Food;
from scoreboard import ScoreBoard;

screen = Screen();
screen.bgcolor('black');
screen.setup(width=600, height=600)
screen.tracer(0);


my_snake = Snake();
new_food = Food();
score_board = ScoreBoard();



screen.listen();

screen.onkey(key="Up", fun=my_snake.up)
screen.onkey(key="Down", fun=my_snake.down)
screen.onkey(key="Left", fun=my_snake.left)
screen.onkey(key="Right", fun=my_snake.right)



is_game_on = True;

while is_game_on:
    screen.update()
    time.sleep(0.1);

    my_snake.move();

    #Detect collision with food
    if my_snake.head.distance(new_food) < 15:
        new_food.new_spot();
        score_board.add_score();
        my_snake.extend();
    
    #Detect collision with wall
    if my_snake.head.xcor() > 290 or my_snake.head.xcor() < -290 or my_snake.head.ycor() > 290 or my_snake.head.ycor() < -290:
        is_game_on = False;
        score_board.game_over();

    #Detect collision with tail

    for item in my_snake.my_snakes[1:]:
        if my_snake.head.distance(item) < 15:
            score_board.game_over();
            is_game_on = False;


screen.exitonclick();