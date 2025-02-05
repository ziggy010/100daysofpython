import smtplib;
import datetime as dt;
import random;

my_email = '9813110577r@gmail.com';
my_password = 'qxslssfgrvvcnnjd';

now = dt.datetime.now();
weekday = now.weekday();

with open('Day 32/quotes.txt') as file:
    quotes_list = file.readlines();
    random_quote = random.choice(quotes_list);

if weekday == 1:
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls();
        connection.login(user=my_email, password=my_password);
        connection.sendmail(from_addr=my_email, to_addrs='duwalkrisha35@gmail.com', msg=f'Subject:Happy Tuesday\n\nHello cuite pie\n\n{random_quote}');
else:
    print("It's not tuesday");


