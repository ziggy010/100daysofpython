from turtle import Turtle;
import random;

class Food(Turtle):
    def __init__(self):
        super().__init__();
        self.shape('turtle');
        self.penup();
        self.color('orange');
        self.shapesize(stretch_len=0.5, stretch_wid=0.5);
        self.setheading(45);
        self.new_food();

    def new_food(self):
        self.x = random.randint(-280, 280);
        self.y = random.randint(-280,280);
        self.goto(self.x, self.y);

