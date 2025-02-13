from selenium import webdriver;
from selenium.webdriver.common.by import By;
from selenium.webdriver.common.keys import Keys;
from selenium.webdriver.common.action_chains import ActionChains;
from dotenv import load_dotenv;
import time;
import os;

load_dotenv();

chrome_options = webdriver.ChromeOptions();
chrome_options.add_experimental_option('detach', True);
chrome_options.binary_location = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"

driver = webdriver.Chrome(options=chrome_options);
driver.get('https://www.linkedin.com/jobs/search/?currentJobId=4142524743&distance=25&f_AL=true&geoId=104630404&keywords=python&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true');

time.sleep(4);
ActionChains(driver).send_keys(Keys.ESCAPE).perform();
time.sleep(1);

sign_in_button = driver.find_element(By.XPATH, value="/html/body/div[1]/header/nav/div/a[2]");
sign_in_button.click();
time.sleep(2);

email_field = driver.find_element(By.ID, value='username');
email_field.send_keys(os.environ.get('email'));

password_field = driver.find_element(By.ID, value='password');
password_field.send_keys(os.environ.get('password'));

final_sign_in_button = driver.find_element(By.XPATH, value='//*[@id="organic-div"]/form/div[4]/button');
final_sign_in_button.click();

save_button = driver.find_element(By.CLASS_NAME, value='jobs-save-button');
save_button.click();

time.sleep(1);

company_page = driver.find_element(By.CSS_SELECTOR, value='.job-details-jobs-unified-top-card__company-name a');
company_page.click();

time.sleep(2);

print('page loaded');

follow_button = driver.find_element(By.CSS_SELECTOR, value='.org-top-card-primary-actions__inner button');
follow_button.click();

