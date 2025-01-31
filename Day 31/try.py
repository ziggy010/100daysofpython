import pandas;
import random;

data = pandas.read_csv('Day 31/data/french_words.csv');

data_list = data.to_dict(orient = 'records');

random_word = random.choice(data_list);

print(random_word['English']);
print(random_word['French']);

