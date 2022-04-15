from typing import OrderedDict

from selenium import webdriver
from selenium.webdriver.common.by import By

session = webdriver.Chrome()

session.get("https://las.op.gg/champions")
champion_list = session.find_element(By.XPATH, '//nav[@class="css-pqbqz6 e1n0mtzi8"]')
url_list = []
for element in champion_list.find_elements(By.XPATH, '//a'):
    url = element.get_attribute("href")
    if "/champions/" in url:
        url_list.append('    \'' + url + '\',')
url_list = list(OrderedDict.fromkeys(url_list))
url_list.sort()
for url in url_list:
    print(url)

session.close()
