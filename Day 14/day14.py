import art;
import random;
import game_date as gd;
import os;

print(art.logo);

data_one = random.choice(gd.data);
data_two = random.choice(gd.data);

game_status = True;
score = 0;


while game_status:

    print(f"\nCompare A: {data_one['name']}, a {data_one['description']}, from {data_one['country']}, {data_one['follower_count']} ")

    print(art.vs);

    print(f"\nCompare B: {data_two['name']}, a {data_two['description']}, from {data_two['country']}, {data_two['follower_count']} ")


    user_guess = input("\nWho has more followers? Type 'A' or 'B': ")

    if user_guess == 'A':
        if data_one['follower_count'] > data_two['follower_count']:
            score += 1;
            print(f"\nYou're right! Current Score: {score}");
            data_one = data_two;
        else:
            os.system('clear');
            print(art.logo);
            print(f"\nSorry, that's wrong. Final score: {score}");
            game_status = False;

    elif user_guess == 'B':
        if data_two['follower_count'] > data_one['follower_count']:
            score += 1;
            print(f"\nYou're right! Current Score: {score}");
            data_one = data_two;
        else:
            os.system('clear');
            print(art.logo);
            print(f"\nSorry, that's wrong. Final score: {score}");

            game_status = False;
    else:
        print("wrong entry")
        game_status = False;
    
    data_two = random.choice(gd.data);










