import random;
import art;

print(art.logo);

print("\nWelcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

random_number = random.randint(1,100);

lives = 0;

difficulty = input("\nChoose a difficulty. type 'easy' or 'hard': ")

if difficulty == 'easy':
    lives = 10;
else:
    lives = 5;

game_status = True;

while game_status:
    print(f"\nYou have {lives} attempts remaining to guess the number.")
    user_guess = int(input("\nMake a guess: "));
    if user_guess > random_number:
        print("\nToo high.\nGuess Again.");
        lives -= 1;
    elif user_guess < random_number:
        print("\nToo low.\nGuess again.");
        lives -= 1;
    else:
        print(f"\nYou got it! The answer was {random_number}.")
        game_status = False;
    
    if lives == 0:
        print("\nYou ran out of lives. Game over!")
        game_status = False;

