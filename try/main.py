from turtle import Turtle, Screen;
from paddle import Paddle;
from ball import Ball;
import time;


screen = Screen();
screen.bgcolor('black');
screen.setup(width=800, height=600);
screen.tracer(0);
screen.listen();

#right paddle
r_paddle = Paddle(position=(370,0));
screen.onkey(fun=r_paddle.move_up, key="Up");
screen.onkey(fun=r_paddle.move_down, key="Down");


#left paddle 
l_paddle = Paddle(position=(-370,0));
screen.onkey(fun=l_paddle.move_up, key="w");
screen.onkey(fun=l_paddle.move_down, key="s");

#ball

ball = Ball();
another_ball = Ball();

is_game_on = True;

while is_game_on:
    screen.update();
    time.sleep(0.1);
    ball.move_ball();

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_collide();

    if ball.xcor() > 340 and ball.distance(r_paddle) < 40:
        ball.paddle_collide();

    if ball.xcor() < -340 and ball.distance(l_paddle) < 40:
        ball.paddle_collide();



screen.exitonclick();