import pandas;

my_data = pandas.read_csv('Day 30/nato.csv');

user_input = input("Enter a word: ").upper();

data_dict = {row.letter:row.code for index, row in my_data.iterrows()};

final_output = [data_dict[item] for item in user_input];

print(final_output);