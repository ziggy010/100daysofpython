import json;

with open('day 29/revise/data.json') as file:
    data = json.load(file);
    data['Twitter']['Email'] = 'hello';
    print(data);