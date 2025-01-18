from turtle import Turtle;

class Ball(Turtle):
    def __init__(self):
        super().__init__();
        self.color('white');
        self.shape('circle');
        self.penup();
        self.xpos = 10;
        self.ypos = 10;
    
    def move_ball(self):
        new_x = self.xcor() + self.xpos;
        new_y = self.ycor() + self.ypos;
        self.goto(new_x, new_y);

    def wall_collide(self):
        self.ypos *= -1;
    
    def paddle_collide(self):
        self.xpos *= -1;