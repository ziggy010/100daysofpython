from turtle import Turtle;

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__();
        self.position = position;
        self.shape('square');
        self.shapesize(stretch_len=0.5, stretch_wid=5);
        self.color('white');
        self.penup();
        self.goto(self.position);

    def moveUp(self):
        new_y = self.ycor() + 20;
        self.goto(self.xcor(), new_y);

    def moveDown(self):
        new_y = self.ycor() - 20;
        self.goto(self.xcor(), new_y);