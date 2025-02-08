import requests;
import os;

def send_text(bot_message):
    bot_token = os.environ.get("bot_token_api");
    bot_chatID = os.environ.get("bot_chat_id");
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message;

    response = requests.get(send_text);
    response.raise_for_status();

    return response.json();


test = send_text('Drink water myau myau');


