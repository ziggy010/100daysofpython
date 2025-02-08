import requests;

def send_text(bot_message):
    bot_token = '7431352522:AAHzOxR8taeYZyx7cfnjeaO7hYxV1xNtvDg';
    bot_chatID = '347333390';
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message;

    response = requests.get(send_text);
    response.raise_for_status();

    return response.json();


test = send_text('Drink water myau myau');


