import pandas;
import random;



my_data = pandas.read_csv('Day 31/data/french_words.csv');
data_dict = my_data.to_dict('records');

random_data = random.choice(data_dict)['French'];

print(random_data);