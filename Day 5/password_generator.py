import random;

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

user_letters = int(input("\nHow many letters would you like in your passwords?\n- "))
user_symbols = int(input("\nHow many symbols do you want in your password?\n- "))
user_numbers = int(input("\nHow many numbers would you like in your password?\n- "))

user_password = []

for letter in range(0, user_letters):
    user_password.append(random.choice(letters));

for letter in range(0, user_symbols):
    user_password.append(random.choice(symbols));

for letter in range(0, user_numbers):
    user_password.append(random.choice(numbers));

final_password = "";

random.shuffle(user_password);

for password in user_password:
    final_password += password;


print("\nYour final password is\n-", final_password);
print("\nThank you for generating password with us!\n")

