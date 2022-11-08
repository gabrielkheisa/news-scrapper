import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime
import base64
import json
import urllib.parse

from selenium.webdriver.chrome.options import Options

key = "API_KEY" 

while(1):
    try:
        now = datetime.now()
        dt_string = now.strftime("%d-%m-%Y %H:%M:%S")

        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        browser = webdriver.Chrome(executable_path="/usr/bin/chromedriver", chrome_options=options) 

        browser.delete_all_cookies()
        browser.get("https://en.antaranews.com/")

        browser.implicitly_wait(5)

        berita1 = browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[3]/div[1]/section[1]/div/div[2]/div/div/div[1]/article[1]/header/h3/a").get_attribute('textContent')
        berita2 = browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[3]/div[1]/section[1]/div/div[2]/div/div/div[1]/article[2]/header/h3/a").get_attribute('textContent')
        berita3 = browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[3]/div[1]/section[1]/div/div[2]/div/div/div[1]/article[3]/header/h3/a").get_attribute('textContent')
        berita4 = browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[3]/div[1]/section[1]/div/div[2]/div/div/div[1]/article[4]/header/h3/a").get_attribute('textContent')



        #Quick copy
        #browser.find_element_by_xpath("").get_attribute('')

        news = {
            "server_update": dt_string,
            "news": [
              {
                "judul": berita1,
                "berita": "",
                "URL": browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[3]/div[1]/section[1]/div/div[2]/div/div/div[1]/article[1]/header/h3/a").get_attribute('href'),
                "gambar": browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[3]/div[1]/section[1]/div/div[2]/div/div/div[1]/article[1]/div/a/picture/img").get_attribute('src'),
                "tgl": browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[3]/div[1]/section[1]/div/div[2]/div/div/div[1]/article[1]/header/p/span").get_attribute('textContent')
              },
              {
                "judul": berita2,        
                "berita": "",
                "URL": browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[3]/div[1]/section[1]/div/div[2]/div/div/div[1]/article[2]/header/h3/a").get_attribute('href'),
                "gambar": browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[3]/div[1]/section[1]/div/div[2]/div/div/div[1]/article[2]/div/a/picture/img").get_attribute('src'),
                "tgl": browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[3]/div[1]/section[1]/div/div[2]/div/div/div[1]/article[2]/header/p/span").get_attribute('textContent')
              },
              {
                "judul": berita3,        
                "berita": "",
                "URL": browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[3]/div[1]/section[1]/div/div[2]/div/div/div[1]/article[3]/header/h3/a").get_attribute('href'),
                "gambar": browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[3]/div[1]/section[1]/div/div[2]/div/div/div[1]/article[3]/div/a/picture/img").get_attribute('src'),
                "tgl": browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[3]/div[1]/section[1]/div/div[2]/div/div/div[1]/article[3]/header/p/span").get_attribute('textContent')
              },
              {
                "judul": berita4,        
                "berita": "",
                "URL": browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[3]/div[1]/section[1]/div/div[2]/div/div/div[1]/article[4]/header/h3/a").get_attribute('href'),
                "gambar": browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[3]/div[1]/section[1]/div/div[2]/div/div/div[1]/article[4]/div/a/picture/img").get_attribute('src'),
                "tgl": browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[3]/div[1]/section[1]/div/div[2]/div/div/div[1]/article[4]/header/p/span").get_attribute('textContent')
              }
            ]
        }

        news = json.dumps(news)

        print(news)
        news = urllib.parse.quote_plus(news)

        response = requests.get('https://api.gabrielkheisa.xyz/news/antaranews/index.php?key='+ key +'&news='+ news)

        browser.quit()
        print("Sleep for 1 hour")
        time.sleep(60*60)
    except:
        print("Error gak jelas, skip")
        browser.quit()
        print("Sleep for 1 hour")
        time.sleep(60*60)

