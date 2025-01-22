from turtle import Turtle;
import random;

COLORS = ['black', 'red', 'purple', 'blue', 'green', 'orange', 'brown'];
STARTING_MOVE = 5;
MOVE_INCREMENT = 10;

class Car():
    def __init__(self):
        self.all_cars = [];
        self.car_speed = STARTING_MOVE;

    def create_car(self):
        random_number = random.randint(1,6);
        if random_number == 1:
            new_car = Turtle(shape='square');
            new_car.penup();
            new_car.color(random.choice(COLORS));
            new_car.shapesize(stretch_len=2, stretch_wid=0.8);
            new_car.setheading(180);
            random_y = random.randint(-250, 250);
            new_car.goto(300, random_y);    
            self.all_cars.append(new_car);

    def move_cars(self):
        for item in self.all_cars:
            item.forward(self.car_speed);
    
    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT;

    