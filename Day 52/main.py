from bs4 import BeautifulSoup;
import requests;
from selenium import webdriver;
from selenium.webdriver.common.by import By;
import time;

chrome_options = webdriver.ChromeOptions();
chrome_options.add_experimental_option('detach', True);
chrome_options.binary_location = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser";

# driver = webdriver.Chrome(options=chrome_options);


response = requests.get('https://appbrewery.github.io/Zillow-Clone/');

soup = BeautifulSoup(response.text, 'html.parser');

price_list = [item.getText().replace("/mo", '').split('+')[0] for item in soup.find_all(class_ = 'PropertyCardWrapper__StyledPriceLine')];

address = [item.getText().strip() for item in soup.find_all(attrs={'data-test': 'property-card-addr'})];

link = [item['href'].strip() for item in soup.find_all(class_ = 'StyledPropertyCardDataArea-anchor')];

print(price_list)   ;


# driver.get('https://forms.gle/wtLTnxhkpRSAnidq8');


# time.sleep(5);


# for i in range(len(price_list)):
#     property_address_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input');
#     price_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input');
#     property_link_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input');
#     submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div');

#     property_address_field.send_keys(address[i]);
#     price_field.send_keys(price_list[i]);
#     property_link_field.send_keys(link[i]);

#     time.sleep(1);

#     submit_button.click();

#     time.sleep(3);

#     submit_next = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a');
#     submit_next.click();

#     time.sleep(2);



