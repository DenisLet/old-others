import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
link = "https://www.basketball24.com/match/4Kg6dKHe/#/match-summary/match-summary"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    links = browser.find_elements(By.CSS_SELECTOR,"a.participant__participantName")
    class Participants:
        home_link = links[0].get_attribute("href")
        away_link = links[1].get_attribute("href")
    print(Participants.away_link)
finally:
    time.sleep(20)
    browser.quit()
