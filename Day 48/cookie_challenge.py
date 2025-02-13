from selenium import webdriver;
from selenium.webdriver.common.by import By;
from time import time;


chrome_options = webdriver.ChromeOptions();
chrome_options.add_experimental_option('detach', True);

driver = webdriver.Chrome(options=chrome_options);
driver.get('https://orteil.dashnet.org/experiments/cookie/');

cookie = driver.find_element(By.ID, value='cookie');

total_time = time() + 5*60;

while True:
    timeout = time() + 5;
    while time() < timeout:
        cookie.click();
    
    all_available_items = driver.find_elements(By.CSS_SELECTOR, value='#store div');
    affordable_items = [item for item in all_available_items if item.get_attribute('class') == ""];

    affordable_items[-1].click();
        
    if time() > total_time:
        break;

