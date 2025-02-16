from selenium import webdriver;
from selenium.webdriver.common.by import By;
from selenium.webdriver.common.keys import Keys;
import time;

class InternetSpeedBot:
    def __init__(self):

        chrome_options = webdriver.ChromeOptions();
        chrome_options.add_experimental_option('detach', True);
        chrome_options.binary_location = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser";

        self.username = 'risab_tajale';
        self.password = 'cryptolover5599!'

        self.driver = webdriver.Chrome(options=chrome_options);

    def tweet_bot(self):
        tweet_links = ['https://x.com/THEAIRDROPARC/status/1887949083765338378','https://x.com/THEAIRDROPARC/status/1886445175834321021', 'https://x.com/THEAIRDROPARC/status/1853828730319208594' ]
        self.driver.get('https://twitter.com');
        time.sleep(2);

        sign_in_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[4]/a');
        sign_in_button.click();

        time.sleep(30);

        title = self.driver.find_element(By.XPATH, '//*[@id="modal-header"]/span/span');
        print(title.text);

        username_field = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input');
        username_field.send_keys(self.username);

        next_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]');
        next_button.click();

        time.sleep(2);

        password_field = self.driver.find_element(By.NAME, 'password');
        password_field.send_keys(self.password);

        login_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button');
        login_button.click();

        time.sleep(10);

        for item in tweet_links:
            self.driver.get(item);
            time.sleep(10);

            comment_box = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div');
            comment_box.send_keys("That's great");

            time.sleep(2);

            reply_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button');
            reply_button.click();

            time.sleep(5);

        # tweet_field = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div');
        # tweet_field.send_keys('Hello world, this is bot tweeting');

        # time.sleep(2);

        # post_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button');
        # post_button.click();



    def speed_checker_bot(self):
        self.driver.get('https://fast.com');
        time.sleep(10);
        speed = self.driver.find_element(By.ID, 'speed-value').text;
        return speed;
