import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from functools import reduce


try:
    browser = webdriver.Chrome()
    browser.get(url)
    browser.implicitly_wait(1)
    vars =  browser.find_elements(By.CSS_SELECTOR,"div.filters__tab")
    vars[2].click()
    matches = browser.find_elements(By.CSS_SELECTOR,"[id^='g_1']")
    for i in matches:
        link = i.get_attribute("id")
        url = f"https://www.soccer24.com/match/{link[4:]}"
        print(url)
finally:
    time.sleep(10)
    browser.quit()