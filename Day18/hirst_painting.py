import turtle as t;
import random;

t.colormode(255);

# import colorgram as cg;

# colors = cg.extract('Day18/image.jpg', 25);

colors_list = [(229, 228, 226), (225, 223, 224), (199, 176, 117), (124, 37, 24), (208, 221, 212), (166, 106, 57), (6, 57, 83), (185, 158, 54), (220, 224, 228), (108, 68, 84), (113, 161, 175), (40, 37, 35), (23, 122, 173), (64, 153, 139), (77, 40, 48), (90, 142, 53), (9, 67, 47), (180, 97, 80), (131, 39, 41), (211, 202, 152), (140, 172, 157), (176, 152, 158), (178, 201, 186), (218, 181, 171), (169, 200, 209)];

# for item in range(len(colors)):
#     r = colors[item].rgb.r;
#     g = colors[item].rgb.g;
#     b = colors[item].rgb.b;

#     my_tuple = (r,g,b);

#     colors_list.append(my_tuple);

# print(colors_list);



turtle = t.Turtle();
screen = t.Screen();

turtle.speed("fastest");

turtle.penup();

x_cor = -360;
y_cor = -350;

while not y_cor == 150:
    turtle.goto(x_cor,y_cor);
    for i in range(10):
        turtle.pendown();
        turtle.color(random.choice(colors_list));
        turtle.begin_fill()
        turtle.circle(10);
        turtle.end_fill();
        turtle.penup();
        turtle.forward(50);
    y_cor += 50;

screen.exitonclick();
