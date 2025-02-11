from bs4 import BeautifulSoup;
import requests;


movies_data = requests.get(url='https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/');

soup = BeautifulSoup(movies_data.text, 'html.parser');

all_title = soup.find_all(name = 'h3', class_ = "title");

all_title_list = [item.getText() for item in all_title];

all_title_list.reverse();

with open('Day 45/movies.txt', 'w') as file:
    for title in all_title_list:
        file.write(f"{title}\n")