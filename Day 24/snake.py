from turtle import Turtle;

STARTING_POSITION = [(0,0), (-20,0), (-40,0)];

UP = 90;
LEFT = 180;
DOWN = 270;
RIGHT = 0;


class Snake():
    def __init__(self):
        self.snake_segment = [];
        self.create_snake();
        self.head = self.snake_segment[0];
    

    def add_snake(self, position):
        my_snake = Turtle(shape='square');
        my_snake.color('white');
        my_snake.penup();
        my_snake.goto(position);
        self.snake_segment.append(my_snake);
    
    def create_snake(self):
        for pos in STARTING_POSITION:
            self.add_snake(position=pos);
    
    def reset(self):
        for seg in self.snake_segment:
            seg.goto(1000,1000);
        self.snake_segment.clear();
        self.create_snake();
        self.head = self.snake_segment[0];


    def extend_snake(self):
        x_pos = self.snake_segment[-1].xcor();
        y_pos = self.snake_segment[-1].ycor();

        self.add_snake(position=(x_pos, y_pos));
        
    def move(self):
        for item in range(len(self.snake_segment)-1, 0, -1):
            new_x = self.snake_segment[item-1].xcor();
            new_y = self.snake_segment[item-1].ycor();

            self.snake_segment[item].goto(new_x, new_y);
        
        self.head.forward(20);
    

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP);
    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT);
    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT);
    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN);



    

