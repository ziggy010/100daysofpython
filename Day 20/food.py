from turtle import Turtle;
import random;

class Food(Turtle):
    def __init__(self):
        super().__init__();
        self.shape("circle");
        self.penup();
        self.shapesize(0.5,0.5,1);
        self.color('blue');
        self.speed('fastest');
        self.new_spot();
    
    def new_spot(self):
        self.random_xcor = random.randint(-270,270);
        self.random_ycor = random.randint(-270,270);
        self.goto(self.random_xcor, self.random_ycor);

