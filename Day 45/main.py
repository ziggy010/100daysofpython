# from bs4 import BeautifulSoup;

# with open('Day 45/website.html') as file:
#     data = file.read();

# soup = BeautifulSoup(data, 'html.parser');

# all_anchor_tags = soup.find_all(name='a');

# heading = soup.find(name = 'h1', id = 'name');

# sub_heading = soup.find(name= 'h3', class_ = 'heading');

# company_url = soup.select_one(selector="p a");

# all_heading_class = soup.select(selector='.heading');

# print(all_heading_class);

from bs4 import BeautifulSoup;
import requests;
import heapq;

live_data = requests.get(url='https://news.ycombinator.com/news');

soup = BeautifulSoup(live_data.text, 'html.parser');

all_title = soup.find_all(class_ = "titleline");

text_list = [];
link_list = [];


for item in all_title:
    article_text = item.find('a').getText();
    text_list.append(article_text);
    article_link = item.find('a').get('href');
    link_list.append(article_link);

all_score_list = [int(score.getText().split(" ")[0]) for score in soup.find_all(class_ = 'score')];

highest_score_index = all_score_list.index(max(all_score_list));
top_3 = heapq.nlargest(3, all_score_list);

for item in top_3:
    index = all_score_list.index(item);
    print(f"Title: {text_list[index]}")
    print(f"Link: {link_list[index]}")
    print(f"Upvotes: {all_score_list[index]}");
