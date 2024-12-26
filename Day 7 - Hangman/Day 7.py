import random;

print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/
''')

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list);

place_holder = "";

for i in range(len(chosen_word)):
    place_holder += "_ ";

print(f"\nWord to guess: {place_holder}")

game_over = False;
correct_letters = [];
lives = 6;

while not game_over:
    guess = input("\nGuess the letter: ")

    display = "";

    for letter in chosen_word:
        if letter == guess:
            display += letter;
            correct_letters.append(letter);
        elif letter in correct_letters:
            display += letter;
        else:
            display += "_ "
    
    print(f"\n{display}");

    if guess in chosen_word:
        print(f"\nCorrect letter! You have {lives}/6 lives left!")

    if guess not in chosen_word:
        lives -= 1;
        print(f"\nNot correct, You have {lives}/6 lives left to guess the word!\n")

    if lives <= 0:
        game_over = True;
        print("\nYou lose! Out of lives!\n")

        
    if "_" not in display:
        game_over = True;
        print("\nYou won!\n")

