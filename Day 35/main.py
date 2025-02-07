import requests;

API_KEY = "3999bc7a2f23064293ca6576cfd18a80";


parameters = {
    'appid' : API_KEY,
    'lat' : 27.712017,
    'lon' : 85.312950,
}


response = requests.get('https://api.openweathermap.org/data/2.5/forecast', params=parameters);
response.raise_for_status();

data = response.json()['city'];

print(data);



