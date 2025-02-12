from bs4 import BeautifulSoup;
import requests;

class BillboardManager:
    def __init__(self):
        # user_input = input("What year you would like to travel to? Type the date in this format, YYYY-MM-DD: ")
        user_input = '2025-01-10';
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
        billboard_url = f'https://www.billboard.com/charts/hot-100/{user_input}';
        response = requests.get(url=billboard_url, headers = header);
        soup = BeautifulSoup(response.text, 'html.parser');
        all_title = soup.select("li h3", id='title-of-a-story');
        all_title_list = [item.getText().strip() for item in all_title][0:100];
        print(all_title_list);