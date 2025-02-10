import requests;

SHETTY_GET_ENDPOINT = 'https://api.sheety.co/d5cd771477e5ef9a0030819bc2b6a0e5/flightDealsPython/prices';

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.get_response = requests.get(url=SHETTY_GET_ENDPOINT);
        data_list = self.get_response.json()['prices'];
        # data_list = [{'city': 'Paris', 'iataCode': '', 'lowestPrice': 54, 'id': 2}, {'city': 'Frankfurt', 'iataCode': '1', 'lowestPrice': 42, 'id': 3}, {'city': 'Tokyo', 'iataCode': '', 'lowestPrice': 485, 'id': 4}];


        for item in data_list:
            iata_data = item.get('iataCode');
            if iata_data == "":
                id = item.get('id');
                update_parameters = {
                    'price':{
                        'iataCode' : 'Testing',
                    }
                }
                self.put_response = requests.put(url=f"{SHETTY_GET_ENDPOINT}/{id}", json=update_parameters);
                print(self.put_response.text);



data = DataManager();