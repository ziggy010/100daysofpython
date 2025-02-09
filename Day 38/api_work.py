import requests;
from sheety import SheetyApi;
import os;

APP_ID = os.environ['app_id'];
API_KEY = os.environ['api_key'];
syndigo_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise";
GENDER = 'Male';
WEIGHT_KG = '69';
HEIGHT_CM = '170';
AGE = '22';

header = {
    'x-app-id' : APP_ID,
    'x-app-key' : API_KEY,
}

class ApiWork:
    def __init__(self):

        self.user_input = input('Tell me which exercise you did: ').title();

        self.exercise_parameters = {
            'query' : self.user_input,
            'gender' : GENDER,
            'weight_kg' : WEIGHT_KG,
            'height_cm' : HEIGHT_CM,
            'age' : AGE,
        }

        self.response = requests.post(url= syndigo_endpoint, headers = header, json=self.exercise_parameters);

    def get_exercise(self):
        exercise_data = self.response.json()['exercises'];
        print(self.user_input);

        for item in range(len(exercise_data)):
            name = exercise_data[item]['name'];
            calories = exercise_data[item]['nf_calories'];
            duration = exercise_data[item]['duration_min'];
            sheety_api = SheetyApi(exercise=name, calories=calories, duration=duration);
