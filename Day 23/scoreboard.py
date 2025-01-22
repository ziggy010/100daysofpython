from turtle import Turtle;

FONT = ('verdana', 20, 'italic');

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__();
        self.level = 1;
        self.color('black');
        self.penup();
        self.hideturtle();
        self.score();

    def score(self):
        self.goto(-230, 260);
        self.write(arg=f'Level: {self.level}', align='center', font=FONT);
    
    def update_score(self):
        self.level += 1;
        self.clear();
        self.write(arg=f'Level: {self.level}', align='center', font=FONT);
        
    
    def game_over(self):
        self.goto(0,0);
        self.write(arg='Game over', align='center', font=FONT);