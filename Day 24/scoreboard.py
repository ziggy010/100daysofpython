from turtle import Turtle;

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__();
        self.score = 0;
        self.high_score = 0;
        self.color('white');
        self.penup();
        self.goto(0, 280);
        self.update_scoreboard();
        self.hideturtle();

    def update_scoreboard(self):
        self.clear();
        self.write(arg=f"Score: {self.score}, High Score: {self.high_score}", align='center', font=('verdana', 18, 'italic'));
    
    def update_score(self):
        self.score += 1;
        self.update_scoreboard();

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score;
        self.score = 0;
        self.update_scoreboard();

    

        
    
        