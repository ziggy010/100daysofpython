from selenium import webdriver;
from selenium.webdriver.common.by import By;
from selenium.webdriver.common.keys import Keys;

chrome_options = webdriver.ChromeOptions();
chrome_options.add_experimental_option('detach', True);

driver = webdriver.Chrome(options=chrome_options);
driver.get('https://en.wikipedia.org/wiki/Main_Page');

# active_editors = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[1]/a');

# active_editors.click();

# view_source = driver.find_element(By.LINK_TEXT, value='View source');

# view_source.click();

search_bar = driver.find_element(By.NAME, value='search');

search_bar.send_keys("Python", Keys.ENTER);
