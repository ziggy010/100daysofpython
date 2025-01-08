from turtle import Turtle, Screen;
import random;

screen = Screen();
screen.setup(width=500, height=400);
screen.bgcolor('black');
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ");
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple'];
all_turtle = [];
is_game_on = False;

y = -50;

for i in range(len(colors)):
    turtle = Turtle(shape="turtle");
    turtle.penup();
    turtle.color(colors[i]);
    turtle.goto(x = -240, y = y);
    y += 30;
    all_turtle.append(turtle);

if user_bet:
    is_game_on = True;

while is_game_on:

    for item in all_turtle:
        if item.xcor() >= 220:
            is_game_on = False;
            print(item.xcor());
            winner = item.color()[0];
            if user_bet == winner:
                print("\nYour turtle won the race!")
            else:
                print(f"\n{winner} is the winner!, you Lost!")

        random_number = random.randint(0,10);
        item.forward(random_number);







screen.exitonclick();