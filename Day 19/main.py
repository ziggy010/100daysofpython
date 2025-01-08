from turtle import Turtle, Screen;

turtle = Turtle();
screen = Screen();

def forward():
    turtle.forward(10);

def backward():
    turtle.backward(10);

def clockwise():
    turtle.left(20);

def anti_clockwise():
    turtle.right(20);

def clear_screen():
    turtle.reset();
    turtle.home();

screen.listen();

screen.onkey(key="w", fun=forward);
screen.onkey(key="s", fun=backward);
screen.onkey(key="a", fun=clockwise);
screen.onkey(key="d", fun=anti_clockwise);
screen.onkey(key="c", fun=clear_screen);

screen.exitonclick();