from turtle import Turtle, Screen;
from paddle import Paddle;
from ball import Ball;
import time;
from scoreboard import ScoreBoard;

screen = Screen();
screen.bgcolor('black');
screen.setup(width=800, height=600);
screen.title('pong');
screen.tracer(0);
screen.listen();


r_paddle = Paddle(position=(380, 0));
l_paddle = Paddle(position=(-380, 0));

screen.onkey(fun=r_paddle.moveUp,key='Up');
screen.onkey(fun=r_paddle.moveDown,key='Down');
screen.onkey(fun=l_paddle.moveUp,key='w');
screen.onkey(fun=l_paddle.moveDown,key='s');

#creating ball

ball = Ball();

#creating scoreboard

score_board = ScoreBoard();


is_game_on = True;

while is_game_on:
    screen.update();
    time.sleep(ball.ball_speed);
    ball.moveBall();

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounceBall();

    if ball.xcor() > 360 and ball.distance(r_paddle) < 50:
        ball.bounceFromPaddle();
    
    if ball.xcor() < -360 and ball.distance(l_paddle) < 50:
        ball.bounceFromPaddle();
    
    #detects ball miss from r_paddle.

    if ball.xcor() > 390:
        ball.resetBall();
        time.sleep(1);
        ball.bounceFromPaddle();
        score_board.l_update();

    #detects ball miss from l_paddle.
    
    if ball.xcor() < -390:
        ball.resetBall();
        time.sleep(1);
        ball.bounceFromPaddle();
        score_board.r_update();
        




screen.exitonclick();