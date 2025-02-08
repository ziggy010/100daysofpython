import requests;

API_KEY = "3999bc7a2f23064293ca6576cfd18a80";


parameters = {
    'appid' : API_KEY,
    'lat' : 27.6711133,
    'lon' : 85.4261675,
    'cnt' : 4,
}

response = requests.get('https://api.openweathermap.org/data/2.5/forecast', params=parameters);
response.raise_for_status();

data = response.json();

weather_id_list = [data['list'][item]['weather'][0]['id'] for item in range(0,4)];

def is_raining():
    for item in weather_id_list:
        if item < 700:
            return True;
        else:
            return False;


if is_raining():
    print('Bring umbrella');
else:
    print("you're good");




