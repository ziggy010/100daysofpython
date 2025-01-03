import art;
import random;

print(art.logo);

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10];

def randomCards():
    return random.choice(cards);

player_wants = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ")

game_status = False;

if player_wants == 'y':
    game_status = True;

user_cards = [randomCards(), randomCards()];
computer_cards = [randomCards(), randomCards()];

while game_status:

    user_total = sum(user_cards);
    computer_total = sum(computer_cards);

    print(f"\nYour cards: {user_cards}, current score: {sum(user_cards)} ");
    print(f"\nComputer's first card: {computer_cards[0]}");

    if user_total == 21:
        print("\nYou won with a blackjack!\n")
        game_status = False;
    elif computer_total == 21:
        print("\nComputer won with a blackjack!\n")
        game_status = False;
    
    if user_total > 21:
        print("\nYou lost the game!\n")
        game_status = False;
    
    another_card = input("Type 'y' to get another card, type 'n' to pass: ")

    if another_card == 'n':
        while computer_total < 17:
            computer_cards.append(randomCards())
            computer_total = sum(computer_cards);
        
        if computer_total > 21:
            print("\nYou won! Because computer total is: ", computer_total);
            game_status = False;
        else:
            if user_total == computer_total:
                print("\nDraw! Money back!")
            elif user_total > computer_total:
                print("\nYou won, Computer lose!\n")
            else:
                print("\nYou lose!, computer won!\n")
        print(f"\nYour score: {user_total}, computer score: {computer_total}")
        game_status = False;
    else:
        user_cards.append(randomCards());
        
            
        
            


    


    


