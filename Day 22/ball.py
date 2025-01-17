from turtle import Turtle;



class Ball(Turtle):
    def __init__(self):
        super().__init__();
        self.shape('circle');
        self.color('white');
        self.penup();
        self.x_move = 10;
        self.y_move = 10;
        self.ball_speed = 0.1

    def moveBall(self):
        new_x = self.xcor() + self.x_move;
        new_y = self.ycor() + self.y_move;
        self.goto(new_x, new_y);

    def bounceBall(self):
        self.y_move *= -1;
    
    def bounceFromPaddle(self):
        self.x_move *= -1;
        if self.ball_speed > 0.05:
            self.ball_speed -= 0.01;

    def resetBall(self):
        self.home();