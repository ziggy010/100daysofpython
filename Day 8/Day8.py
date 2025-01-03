import art;

print(art.logo);

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(encode_decode, original_text, shift_amount):
    final_output = "";

    if encode_decode == "decode":
        shift_amount *= -1;

    for letter in original_text:

        if letter in alphabet:

            shifted_index = alphabet.index(letter) + shift_amount;
            shifted_index %= len(alphabet);
            final_output += alphabet[shifted_index];

        else:
            final_output += letter;

    print(f"\nHere is your {encode_decode}d message: {final_output}");

game_status = True;

while game_status:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower();
    text = input("Type your message: \n- ").lower();
    shift = int(input("Type the shift number:\n- "))


    caesar(direction, text, shift);

    restart_game = input("\nType 'yes' if you want to go again. Otherwise type 'no': ").lower();
    
    if restart_game == "no":
        print("\nThank you for using caser cypher!\n");
        game_status = False;
        


