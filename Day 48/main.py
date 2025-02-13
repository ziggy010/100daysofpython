from selenium import webdriver;
from selenium.webdriver.common.by import By;

#preventing to close the chrome automatically

chrome_options = webdriver.ChromeOptions();
chrome_options.add_experimental_option('detach', True);


driver = webdriver.Chrome(options=chrome_options);
# driver.get('https://www.amazon.in/GRAPEWOOD-Airdic-Seater-Living-Premium/dp/B0C94C6YGG/?_encoding=UTF8&pd_rd_w=X45zj&content-id=amzn1.sym.9ec81c8d-2371-4cd0-8126-5b80aa4d313c&pf_rd_p=9ec81c8d-2371-4cd0-8126-5b80aa4d313c&pf_rd_r=JVM2S62XJVG05NE16Q47&pd_rd_wg=ln1iQ&pd_rd_r=808fc32a-fdfe-4658-b6ee-d931b7c5e1ff&ref_=pd_hp_d_btf_ls_gwc_pc_en2_');
driver.get('https://python.org');

# search_bar = driver.find_element(By.CLASS_NAME, value='gLFyf');

# search_button = driver.find_element(By.NAME, value='btnK');

# print(search_button.get_attribute('role'));

# link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget p a");

xpath_link = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[5]/a');

print(xpath_link.get_attribute('href'));

driver.quit();