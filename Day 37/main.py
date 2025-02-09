import requests;
import datetime as dt;
import random;

TOKEN = 'qwerty12345';
USERNAME = 'ziggy';
pixela_endpoint = 'https://pixe.la/v1/users';

user_parameters = {
    'token' : TOKEN,
    'username' : USERNAME,
    'agreeTermsOfService' : 'yes',
    'notMinor' : 'yes',
}

# response = requests.post(url=pixela_endpoint, json=user_parameters);

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs";

header = {
    'X-USER-TOKEN' : TOKEN,
}

graph_parameters = {
    'id' : 'graph1',
    'name' : 'Coding Graph',
    'unit' : 'Hour',
    'type' : 'float',
    'color' : 'ajisai',
}

# response = requests.post(url=graph_endpoint, json = graph_parameters, headers = header);
# print(response.text);


today = (dt.datetime.now()).strftime('%Y%m%d');

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1";

pixel_parameters = {
    'date' : today,
    'quantity' : f"{random.randint(1,5)}",
}

# response = requests.post(url=pixel_endpoint, json=pixel_parameters, headers = header);


update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today}";

update_pixel_parameter = {
    'quantity' : '0.5',
}

# update_response = requests.put(url=update_pixel_endpoint, json=update_pixel_parameter, headers = header);
for i in range(10,0, -1):   

    date = (dt.datetime.now() - dt.timedelta(days=i)).strftime('%Y%m%d');

    delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{date}";

    delete_response = requests.delete(url=delete_endpoint, headers = header);
    print(delete_response.text);
