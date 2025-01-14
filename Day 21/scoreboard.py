from turtle import Turtle;

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__();
        self.color('white');
        self.penup();
        self.goto(0, 275);
        self.score = 0;
        self.write(arg=f"Score: {self.score} ", align="center", font=("verdana", 20, "italic"));
        self.hideturtle();
    
    def add_score(self):
        self.score += 1;
        self.clear();
        self.write(arg=f"Score: {self.score} ", align="center", font=("verdana", 20, "italic"));

    def game_over(self):
        self.goto(0,0);
        self.write(arg="Game Over!", align="center", font=("verdana", 20, "italic"));
