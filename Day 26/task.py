import pandas;

my_data = pandas.read_csv('Day 26/nato.csv');

my_dict = {row.letter:row.code for (index, row) in my_data.iterrows()};

user_input = input("Enter a word: ").upper();

user_list = [item for item in user_input];

answer_list = [my_dict[letter] for letter in user_list];

print(answer_list);