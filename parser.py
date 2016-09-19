__author__ = 'sp41mer'
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome('/Users/sp41mer/PycharmProjects/FbEmailSearch/chromedriver')

emails = [
    'abramova-ie@yandex.ru',
    'Adeljasun@mail.ru',
    'amin-001@yandex.ru',
    'alexdasya@gmail.com',
    'rail-86@inbox.ru',
    'denstrman@gmail.com',
    'arturlevsha@mail.ru',
    'grakmanova@mail.ru',
    'ildartim@gmail.com',
    'kalinina@bashinform.ru',
    'salyambst@mail.ru',
    'Lerika.m7@gmail.com',
    'litvinovichirina@rambler.ru',
    'mansur_y@mail.ru',
    'albertini@list.ru',
    'valeria-tv@yandex.ru',
    'natalya.ovcharuk@phkp.ru',
    'abaykov@mail.ru',
    '89656536162@mail.ru',
    'Ruslana9108@mail.ru',
    'radik842@mail.ru'
]

urls = []

for email in emails:
    email = email.replace('@','%2540')
    driver.get("https://www.facebook.com/search/str/{}/keywords_users".format(email))
    try:
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_css_selector('img'))
        html = driver.page_source
        soup = BeautifulSoup(html)
        for person in soup.find_all('div', attrs={'id': 'BrowseResultsContainer'}):
            url = person.find('a', attrs={'class': '_fbBrowseXuiResult__profileImageLink'}).get('href')
            urls.append(url)
    except:
        print email

print urls
