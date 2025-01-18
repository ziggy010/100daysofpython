from turtle import Turtle;

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__();
        self.position = position;
        self.y_pos = 0;
        self.color('white');
        self.penup();
        self.shape('square');
        self.shapesize(stretch_len=0.5, stretch_wid=5);
        self.goto(position);


    def move_up(self):
        self.y_pos += 20;
        self.goto(self.xcor(), self.y_pos);

    def move_down(self):
        self.y_pos -= 20;
        self.goto(self.xcor(), self.y_pos);
