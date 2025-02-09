import requests;
import os;

class SendMessage:
    def __init__(self, news_title, news_description, difference):
        self.news_title = news_title;
        self.news_description = news_description;
        self.difference = difference;
        self.get_news();



    def send_telegram_message(self, message):
        self.bot_token_api = os.environ.get('bot_token_api');
        self.bot_chatID = os.environ.get('bot_chat_id');

        self.text_endpoint = 'https://api.telegram.org/bot' + self.bot_token_api + '/sendMessage?chat_id=' + self.bot_chatID + '&parse_mode=Markdown&text=' + message;

        self.text_response = requests.get(self.text_endpoint);
        self.text_response.raise_for_status();

        return self.text_response.json();

    def get_news(self):
        emoji = '';
        if float(self.difference) > 0:
            emoji = "🔺";
        else:
            emoji = "🔻";
        for item in range(0, len(self.news_title)):
            message = f'''
                TSLA : {emoji}{self.difference}
                Headline: {self.news_title[item]}
                Brief: {self.news_description[item]}
            ''';
            self.send_telegram_message(message);
    