import requests;
import datetime as dt;
import os;

SHEETY_POST_ENDPOINT = os.environ['sheety_endpoint'];
BEARER_TOKEN = os.environ.get('bearer_token');

class SheetyApi:
    def __init__(self, exercise, duration, calories):
        self.today = dt.datetime.now().strftime("%d/%m/%Y");
        self.time = dt.datetime.now().strftime("%X");
        self.exercise = exercise;
        self.duration = duration;
        self.calories = calories;
        self.header = {
            "Authorization" : f"Bearer {BEARER_TOKEN}",
        }
        self.sheety_parameters = {
            "workout" : {
                'date' : self.today,
                'time' : self.time,
                'exercise' : self.exercise,
                'duration' : self.duration,
                'calories' : self.calories,
            }
        }
        response = requests.post(url=SHEETY_POST_ENDPOINT, json=self.sheety_parameters, headers = self.header);
        response.raise_for_status();
        print(response.text);
