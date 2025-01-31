import pandas;

my_data = pandas.read_csv("Day 30/nato.csv");

my_dict = {row.letter:row.code for index, row in my_data.iterrows()};

def generate():
    user_input = input("Enter a word: ").upper();

    try:
        user_list = [my_dict[item] for item in user_input];
    except KeyError:
        print("sorry, only letters in the alphabet please.");
        generate();
    else:
        print(user_list);


generate();