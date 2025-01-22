from turtle import Turtle;
import random;

class Food(Turtle):
    def __init__(self):
        super().__init__();
        self.create_food();
        
    
    def create_food(self):
        self.random_y = random.randint(-280, 280);
        self.random_x = random.randint(-380, 380);
        self.shape('turtle');
        self.color('orange');
        self.setheading(45);
        self.shapesize(stretch_len=0.8, stretch_wid=0.8);
        self.penup();
        self.goto(self.random_x, self.random_y);
