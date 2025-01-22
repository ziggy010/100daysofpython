#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("quiz/Input/Names/invited_names.txt") as names_file:
    names_list = [];
    names = names_file.readlines();
    for item in names:
        names_list.append(item.replace("\n", ""));

def replaceName(name):
    with open("quiz/Input/Letters/starting_letter.txt") as letter_file:
        letter = letter_file.read();

        updated_content = letter.replace('[name]', name);

    with open(f"quiz/Output/ReadyToSend/{name}.txt", 'w') as file:
        file.write(updated_content);


for name in names_list:
    replaceName(name);






