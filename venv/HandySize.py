from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from functools import reduce
import time

start = time.time()
def creation():
    try:
        url = "https://www.handball24.com"
        browser = webdriver.Chrome()
        browser.get(url)
        resume = input("Select matches and press enter to continue ")
        browser.implicitly_wait(1)
        matches = browser.find_elements(By.CSS_SELECTOR,"[id^='g_7']")
        checklist = list()
        for i in matches:
            link = i.get_attribute("id")
            urls = f"https://www.handball24.com/match/{link[4:]}"
            checklist.append(urls)
    finally:
        browser.quit()
    return checklist

schedule = creation()
caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "eager"
b = webdriver.Chrome(desired_capabilities=caps)
def main(url,browser):

    browser.get(url)
    browser.implicitly_wait(1)
    team_home =browser.find_elements(By.CSS_SELECTOR,"a.participant__participantName")[0].get_attribute(
        "href") +"/results/"
    team_away = browser.find_elements(By.CSS_SELECTOR, "a.participant__participantName")[1].get_attribute(
        "href") + "/results/"
    print(team_home)
    print(team_away)

for i in schedule:
    main(i,b)