import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from functools import reduce
def creation():
    url = "https://www.soccer24.com"
    browser = webdriver.Chrome()
    browser.get(url)
    resume = input("Select matches and press enter to continue ")
    browser.implicitly_wait(1)
    matches = browser.find_elements(By.CSS_SELECTOR,"[id^='g_1']")
    checklist = list()
    for i in matches:
        link = i.get_attribute("id")
        urls = f"https://www.soccer24.com/match/{link[4:]}"
        checklist.append(urls)
    return browser,checklist

