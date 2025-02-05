##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import pandas;
import datetime as dt;
import random;
import smtplib;

MY_EMAIL = '9813110577r@gmail.com'
MY_PASSWORD = 'qxslssfgrvvcnnjd';

birthday_data = pandas.read_csv('Day 32/birthdays.csv');

now = dt.datetime.now();
month = now.month;
day = now.day;

selected_months = birthday_data[birthday_data['month'] == month];

selected_day = selected_months[selected_months['day'] == day];
                

if selected_day.empty:
    print('No birthdays');
else:
    letters_list = ['Day 32/letter_templates/letter_1.txt', 'Day 32/letter_templates/letter_2.txt', 'Day 32/letter_templates/letter_3.txt'];
    random_letter = random.choice(letters_list);
    with open('random_letter') as file:
        data = file.read();
        name = selected_day.name.item();
        email = selected_day.email.item();
        new_data = data.replace('[NAME]', name);
        print(email);

    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls();
        connection.login(user = MY_EMAIL, password= MY_PASSWORD);
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=email, msg=f'Subject:Happy Birthday {name}!\n\n{new_data}');
