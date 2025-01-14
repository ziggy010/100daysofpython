from turtle import Turtle;

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__();
        self.position = position;
        self.my_paddle = [];
        self.shape('square');
        self.color('white');
        self.penup();
        self.speed('fastest');
        self.shapesize(stretch_len=0.5, stretch_wid=5);
        self.goto(position);
    

    def move_up(self):
        new_ycor = self.ycor() + 20;
        self.goto(self.xcor(), new_ycor);
    
    def move_down(self):
        new_ycor = self.ycor() - 20;
        self.goto(self.xcor(), new_ycor);
