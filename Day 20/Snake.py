from turtle import Turtle;

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)];
MOVE_DISTANCE = 20;
UP = 90;
DOWN = 270;
LEFT = 180;
RIGHT = 0;


class Snake:
    def __init__(self):
        self.my_snakes = [];
        self.create_snake();
        self.head = self.my_snakes[0];

    def add_snake(self, item):
        snake = Turtle(shape='square');
        snake.color('white');
        snake.penup();
        snake.goto(item);
        self.my_snakes.append(snake);

    def create_snake(self):
        for item in STARTING_POSITIONS:
            self.add_snake(item);
    
    def extend(self):
        self.add_snake(self.my_snakes[-1].position());
    
    def move(self):
        for item in range(len(self.my_snakes)-1, 0, -1):
            new_xcor = self.my_snakes[item-1].xcor();
            new_ycor = self.my_snakes[item-1].ycor();

            self.my_snakes[item].goto(new_xcor,new_ycor);
        
        self.head.forward(MOVE_DISTANCE);
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP);

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN);
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT);

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT);



        
    