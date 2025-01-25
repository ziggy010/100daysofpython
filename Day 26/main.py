# import random;

# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor'];

# student_score = {item:random.randint(1,100) for item in names};

# high_score = {item:value for (item, value) in student_score.items() if value > 60};

# print(high_score);

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

# result = {word:len(word) for word in sentence.split()}

# print(result);

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day:((temp*9/5) + 32) for (day,temp) in weather_c.items()}

print(weather_f)