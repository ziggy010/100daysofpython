from turtle import Turtle, Screen;
import random;

screen = Screen();
screen.setup(width=500, height=400);
screen.bgcolor('black')
screen.title('Turtle race');
user_bet = screen.textinput(title='Bet on Turtle', prompt='In which turtle you want to make a bet: ')
is_game_on = False;

color = ['red', 'blue', 'yellow', 'purple', 'green', 'white'];
my_turtle = [];

y = -50;

for item in color:
    turtle = Turtle(shape='turtle');
    turtle.color(item);
    turtle.penup();
    turtle.goto(x=-240, y=y);
    y += 30;
    my_turtle.append(turtle);


if user_bet:
    is_game_on = True;

while is_game_on:
    for item in my_turtle:
        random_number = random.randint(0,10);
        item.forward(random_number);

        if item.xcor() >= 235:
            if user_bet == item.color()[0]:
                print("You won the game!")
            else:
                print("Your turtle didn't win the race! the winner is: ", item.color()[0]);
            is_game_on = False;



screen.exitonclick();