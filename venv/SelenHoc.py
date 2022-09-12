from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from functools import reduce
import time
start = time.time()

def creation():
    try:
        url = "https://www.icehockey24.com/"
        browser = webdriver.Chrome()
        browser.get(url)
        resume = input("Select matches and press enter to continue(Add to favorite) ")
        browser.implicitly_wait(1)
        matches = browser.find_elements(By.CSS_SELECTOR,"[id^='g_4']")
        checklist = list()
        for i in matches:
            link = i.get_attribute("id")
            urls = f"https://www.icehockey24.com/match/{link[4:]}"
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

    def separator(matches):
        match_list = list()
        for i in matches:
            line = i.text
            # print(line)
            # if "(" in line or "Awrd" in line:
            #     continue
            # if len([i for i in line.split() if i.isdigit()]) < 6:
            #     continue
            match_list.append(line.split())
        return match_list

    def forming(browser, link1, link2):  # NEED ADD TYPE SPORT AND FIXABLE CSS SELECTOR
        browser.get(link1)
        browser.find_element(By.CSS_SELECTOR,"")
        matches = browser.find_elements(By.CSS_SELECTOR, "[id^='g_4']")
        match_list_home = separator(matches)
        browser.get(link2)
        matches = browser.find_elements(By.CSS_SELECTOR, "[id^='g_4']")
        match_list_away = separator(matches)
        return match_list_home, match_list_away

    games = forming(browser, team_home, team_away)
    for i in games[0]:
        print(i)




for i in schedule:
    main(i,b)
b.quit()