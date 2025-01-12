from turtle import Turtle;
from food import Food;

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__();
        self.color('white');
        self.penup();
        self.sety(y=270);
        self.score = 0;
        self.write(arg=f"Score: {self.score}", align="center", font=("Verdana", 20, "bold"));
        self.hideturtle();
    
    def add_score(self):
        self.score += 1;
        self.clear();
        self.write(arg=f"Score: {self.score}", align="center", font=("Verdana", 20, "bold"));

    def game_over(self):
        self.goto(0,0);
        self.write(arg="Game Over.", align="center", font=("Verdana", 20, "italic"));


    
    



