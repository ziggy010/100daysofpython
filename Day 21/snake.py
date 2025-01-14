from turtle import Turtle;

STARTING_POSITION = [(0,0), (-20, 0), (-40, 0)];
DISTANCE_COVERED = 20;
RIGHT = 0;
UP = 90;
LEFT = 180;
DOWN = 270;


class Snake:
    def __init__(self):
        self.snake_segments = [];
        self.create_snake();
        self.head = self.snake_segments[0];

    
    def add_snake(self, position):
        my_snake = Turtle(shape='square');
        my_snake.color('white');
        my_snake.penup();
        my_snake.goto(position);
        self.snake_segments.append(my_snake);

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_snake(position);

    def extend(self):
        snake_xcor = self.snake_segments[-1].xcor();
        snake_ycor = self.snake_segments[-1].ycor();

        self.add_snake(position=(snake_xcor, snake_ycor));


        
    def move(self):
        for item in range(len(self.snake_segments)-1, 0, -1):
            new_xcor = self.snake_segments[item-1].xcor();
            new_ycor = self.snake_segments[item-1].ycor();
            self.snake_segments[item].goto(new_xcor, new_ycor);
        
        self.head.forward(DISTANCE_COVERED);
    


    def MoveUp(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP);
    def MoveLeft(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT);
    def MoveDown(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN);
    def MoveRight(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT);
