# # with open('Day 25/weather_data.csv') as file:
# #     data = file.readlines();
# #     for item in data:
# #         print(item);

# # import csv;

# # with open('Day 25/weather_data.csv') as file_data:
# #     data = csv.reader(file_data);
# #     temperature = [];
# #     for row in data:
# #         if row[1] != 'temp':
# #             temperature.append(int(row[1]));
    
# #     print(temperature);

# import pandas;
# import numpy;

# data = pandas.read_csv('Day 25/weather_data.csv');

# temp_list = data['temp'];

# # print(temp_list.mean().round(2));

# # print(data['temp'].max());

# # print(data[data.temp == data.temp.max()]);

# monday = data[data.day == 'Monday'];

# celcius = monday.temp[0];


# student = {
#     'student': ['risab', 'krisa'],
#     'score' : [10, 20],
# }

# my_data = pandas.DataFrame(student);

# my_data.to_csv('Day 25/new_data.csv');



import pandas;

data = pandas.read_csv('Day 25/orginal_file.csv');

grey_squirrel = data[data["Primary Fur Color"] == 'Gray'].shape[0];
red_squirrel = data[data["Primary Fur Color"] == 'Cinnamon'].shape[0];
black_squirrel = data[data["Primary Fur Color"] == "Black"].shape[0];

final_data = {
    'Fur Color' : ['grey', 'red', 'black'],
    'Count' : [grey_squirrel, red_squirrel, black_squirrel],
}

csv_data = pandas.DataFrame(final_data);

csv_data.to_csv('Day 25/squirrel_count.csv');
