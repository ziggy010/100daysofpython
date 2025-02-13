from bs4 import BeautifulSoup;
import requests;

class BillboardManager:
    def __init__(self):
        self.user_input = input("What year you would like to travel to? Type the date in this format, YYYY-MM-DD: ")
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
        billboard_url = f'https://www.billboard.com/charts/hot-100/{self.user_input}';
        response = requests.get(url=billboard_url, headers = header);
        soup = BeautifulSoup(response.text, 'html.parser');
        all_title = soup.select("li h3", id='title-of-a-story');
        self.all_title_list = [item.getText().strip() for item in all_title][0:10];
        print(self.all_title_list);

    def get_songs_name(self):
        return self.all_title_list;

    def get_year(self):
        year = self.user_input.split('-')[0];
        return year;
