import turtle as t;
import random;

turtle = t.Turtle();
screen = t.Screen();
t.colormode(255);

direction = [0, 90, 270, 180]


turtle.speed('fastest');
# turtle.pensize(2);

def random_color():
    r = random.randint(0.0,255);
    g = random.randint(0.0,255);
    b = random.randint(0.0,255);

    return (r,g,b);

for i in range(36):
    turtle.circle(80);
    turtle.left(10);
    turtle.color(random_color());


# for i in range(300):
#     turtle.color(random_color());
#     turtle.forward(20);
#     turtle.left(random.choice(direction));

screen.exitonclick();