from selenium import webdriver;
from selenium.webdriver.common.by import By;

chrome_options = webdriver.ChromeOptions();
chrome_options.add_experimental_option('detach', True);

driver = webdriver.Chrome(options=chrome_options);

driver.get('https://python.org');

upcoming_events = driver.find_elements(By.CSS_SELECTOR, value='.event-widget .menu li');

event_dict = {i:{"Date" : upcoming_events[i].text.split("\n")[0], "Event" : upcoming_events[i].text.split("\n")[1]} for i in range(len(upcoming_events))};


print(event_dict);

driver.quit();