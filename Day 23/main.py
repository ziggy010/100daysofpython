from turtle import Screen;
from player import Player;
from car import Car;
import time;
import random;
from scoreboard import ScoreBoard;

screen = Screen();
screen.setup(width=600, height=600);
screen.tracer(0);
screen.listen();

#importing player
player = Player();

#create a car
car = Car();

#create scoreboard
scoreboard = ScoreBoard();

#listening the button
screen.onkey(fun=player.move, key='Up');

is_game_on = True;

while is_game_on:
    time.sleep(0.1);
    screen.update();

    #reseting the player
    if player.ycor() > 280: 
        scoreboard.update_score();
        player.player_reset();
        car.increase_speed();

    car.create_car();
    car.move_cars();

    for item in car.all_cars:
        if player.distance(item) < 20:
            is_game_on = False;
            scoreboard.game_over();





screen.exitonclick();


