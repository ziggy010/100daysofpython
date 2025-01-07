import turtle as t;
import random;

turtle = t.Turtle();
screen = t.Screen();
t.colormode(255);

direction = [0, 90, 270, 180]

turtle.pensize(15);
turtle.speed('fastest');

def random_color():
    r = random.randint(0.0,255);
    g = random.randint(0.0,255);
    b = random.randint(0.0,255);

    return (r,g,b);


for i in range(200):
    turtle.color(random_color());
    turtle.forward(20);
    turtle.left(random.choice(direction));

screen.exitonclick();