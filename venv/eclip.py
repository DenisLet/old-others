import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from functools import reduce
import time
stat = time.time()
url = "https://www.soccer24.com/match/dbl6EBjK/#/match-summary"

try:
    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "eager"
    browser = webdriver.Chrome(desired_capabilities=caps)
    browser.get(url)
    team_home =browser.find_elements(By.CSS_SELECTOR,"a.participant__participantName")[0].get_attribute(
        "href") +"/results/"
    team_away = browser.find_elements(By.CSS_SELECTOR, "a.participant__participantName")[1].get_attribute(
        "href") + "/results/"
    browser.get(team_home)
    browser.get(team_away)
    print(team_home)
    print(team_away)
    # m1 = WebDriverWait(browser,2).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a.event__more.event__more--static")))
    # browser.get(team_away)
    # m2 =  WebDriverWait(browser,2).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a.event__more.event__more--static")))

finally:
    browser.quit()
print(time.time() - stat)