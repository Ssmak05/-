import time
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Serviсe
s=Service('C:\Для хрома\chromedriver-win64\chromedriver.exe')
browser=webdriver.Chrome(service=s)
browser.get("https://www.kinopoisk.ru/lists/movies/top250/?utm_referrer=www.kinopoisk.ru")
time.sleep(10)
html_text=browser.page_sourse
soup=BeautifulSoup(html_text, 'lxml')
print(html_text)
soup.find("base-movie-main-info_mainInfo__ZL_u3")