from bs4 import BeautifulSoup;
import requests;
import smtplib;
import os;
from dotenv import load_dotenv;
import lxml;

#loading env file
load_dotenv();

telegram_user_api = os.environ.get('user_api');
telegram_chat_api = os.environ.get('chat_api');

header= {
      "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",

  "Accept-Encoding": "gzip, deflate, br, zstd",

  "Accept-Language": "en-US,en;q=0.8",

  "Connection": "keep-alive",

  "Sec-Ch-Ua": "\"Not)A;Brand\";v=\"99\", \"Brave\";v=\"127\", \"Chromium\";v=\"127\"",

  "Sec-Ch-Ua-Mobile": "?0",

  "Sec-Ch-Ua-Platform": "\"Windows\"",

  "Sec-Fetch-Dest": "document",

  "Sec-Fetch-Mode": "navigate",

  "Sec-Fetch-Site": "cross-site",

  "Sec-Fetch-User": "?1",

  "Sec-Gpc": "1",

  "Upgrade-Insecure-Requests": "1",

  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
}

website_data = requests.get(url="https://www.amazon.in/GRAPEWOOD-Airdic-Seater-Living-Premium/dp/B0C94C6YGG/?_encoding=UTF8&pd_rd_w=u1ymk&content-id=amzn1.sym.9ec81c8d-2371-4cd0-8126-5b80aa4d313c&pf_rd_p=9ec81c8d-2371-4cd0-8126-5b80aa4d313c&pf_rd_r=FB59G1WJ037KBK60WN13&pd_rd_wg=t06Zn&pd_rd_r=bdb92a6b-7298-4fc6-a903-d69649939e60&ref_=pd_hp_d_btf_ls_gwc_pc_en2_", headers = header);

soup = BeautifulSoup(website_data.text, 'html.parser');

price_data = soup.find(name='span', class_ = "a-price-whole");
print(price_data);

final_price = float(price_data.split('.')[0]);
print(final_price);

target_price = 100.00;


# if price_data < target_price:
    # with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
    #     connection.starttls();
    #     connection.login(user=MY_EMAIL, password=MY_PASSWORD);
    #     connection.sendmail(from_addr=MY_EMAIL, to_addrs='tajale01@gmail.com', msg=f"Subject:Price reached your target\n\nPrice of the product is below {target_price}")

    # message = f"Hello, price for you product has been reached to your target of {target_price}!\nYou can buy it right away!";
    # url = f"https://api.telegram.org/bot{telegram_user_api}/sendMessage?chat_id={telegram_chat_api}&text={message}";
    # response = requests.get(url= url);
    # print(response.json());

