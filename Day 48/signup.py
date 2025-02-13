from selenium import webdriver;
from selenium.webdriver.common.by import By;

chrome_options = webdriver.ChromeOptions();
chrome_options.add_experimental_option('detach', True);

driver = webdriver.Chrome(options=chrome_options);
driver.get('http://secure-retreat-92358.herokuapp.com/');

first_name_field = driver.find_element(By.NAME, value='fName');
last_name_field = driver.find_element(By.NAME, value='lName');
email_field = driver.find_element(By.NAME, value='email');

sign_up_button = driver.find_element(By.CLASS_NAME, value='btn-primary');

first_name_field.send_keys('Risab');
last_name_field.send_keys('Tajale');
email_field.send_keys("tajale01@gmail.com");

sign_up_button.click();