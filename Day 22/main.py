from turtle import Turtle, Screen;
from paddle import Paddle;
from ball import Ball;
import time;


screen = Screen();
screen.bgcolor('black');
screen.setup(width=800, height=600);
screen.listen();
screen.title('pong');
screen.tracer(0);

r_paddle = Paddle(position=(360,0));
l_paddle = Paddle(position=(-360,0));

#creating ball.
ball = Ball();

screen.onkey(fun=r_paddle.move_up, key="Up");
screen.onkey(fun=r_paddle.move_down, key="Down");

screen.onkey(fun=l_paddle.move_up, key="w");
screen.onkey(fun=l_paddle.move_down, key="s");

is_game_on = True;

while is_game_on:
    screen.update();
    time.sleep(0.2);
    ball.moveBall();
    time.sleep(0.1);










screen.exitonclick();