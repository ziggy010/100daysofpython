from turtle import Turtle, Screen;
import random;

turtle = Turtle();
screen = Screen();

turtle.shape('turtle');
colors = ['red', 'black', 'yellow', 'blue', 'green', 'purple', 'brown', 'pink'];

no_of_side = 3;

while no_of_side <= 10:
    for i in range(no_of_side):
        degree = 360/no_of_side
        turtle.left(degree);
        turtle.forward(100);
    no_of_side += 1;
    turtle.color(random.choice(colors))

screen.exitonclick();