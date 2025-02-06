import requests;
import datetime as dt;
import smtplib;
import time;

MY_LAT = 27.712017;
MY_LNG = 85.312950;
MY_EMAIL = '9813110577r@gmail.com'
MY_PASSWORD = 'qxslssfgrvvcnnjd';

parameters = {
    "lat" : MY_LAT,
    "lng" : MY_LNG,
    "formatted" : 0,
}



def iss_up():
    if 80 <= iss_long <= 90 and 23 <= iss_lat <= 32:
        if time_now >= sunset:
            with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
                connection.starttls();
                connection.login(user=MY_EMAIL, password=MY_PASSWORD);
                connection.sendmail(from_addr=MY_EMAIL, to_addrs='tajale01@gmail.com', msg="Subject:ISS IS HERE\n\nhey there ISS is up!");



response = requests.get('https://api.sunrise-sunset.org/json', params=parameters);
response.raise_for_status();
data = response.json()['results'];

iss_response = requests.get('http://api.open-notify.org/iss-now.json');
iss_response.raise_for_status();
iss_data = iss_response.json()['iss_position'];

iss_long = float(iss_data['longitude']);
iss_lat = float(iss_data['latitude']);

sunrise = int(data['sunrise'].split('T')[1].split(':')[0]);
sunset = int(data['sunset'].split("T")[1].split(":")[0]);

time_now = dt.datetime.now().hour;

while True:
    time.sleep(60);
    iss_up();