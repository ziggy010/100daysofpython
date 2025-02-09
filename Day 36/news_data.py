import requests;
import os;
import datetime as dt;

NEWS_API = os.environ.get('news_api');
COMPANY_NAME = "Tesla Inc"

class NewsData():
    def __init__(self):
        self.today = dt.datetime.now().date();
        self.yesterday = self.today - dt.timedelta(days=1);
        self.day_before_yesterday = self.yesterday - dt.timedelta(days=1);
        self.news_parameters = {
            'q' : COMPANY_NAME,
            'from' : f"{str(self.day_before_yesterday)}",
            'to' : f"{str(self.yesterday)}",
            'sortBy' : 'popularity',
            'apikey' : NEWS_API,
        };

        self.news_response = requests.get('https://newsapi.org/v2/top-headlines', params=self.news_parameters);
        self.news_response.raise_for_status();


        self.news_data = self.news_response.json()['articles'];


    def get_news_title(self):
        news_title = [self.news_data[item]['title'] for item in range(len(self.news_data))];
        return news_title;

    def get_news_description(self):
        news_description = [self.news_data[item]['description'] for item in range(len(self.news_data))];    
        return news_description;