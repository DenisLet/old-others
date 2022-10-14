from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
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
        # browser.execute_script("arguments[0].click();", WebDriverWait(browser, 20).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "a.event__more.event__more--static"))))
        # time.sleep(3)
        team1 = browser.find_element(By.CSS_SELECTOR, "div.heading__name").get_attribute("innerHTML")
        matches = browser.find_elements(By.CSS_SELECTOR, "[id^='g_4']")
        match_list_home = separator(matches)
        browser.get(link2)
        # browser.execute_script("arguments[0].click();", WebDriverWait(browser, 20).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "a.event__more.event__more--static"))))
        # time.sleep(3)
        team2 = browser.find_element(By.CSS_SELECTOR, "div.heading__name").get_attribute("innerHTML")
        matches = browser.find_elements(By.CSS_SELECTOR, "[id^='g_4']")
        match_list_away = separator(matches)
        return match_list_home, match_list_away, team1, team2

    games = forming(browser, team_home, team_away)

    home_team_name, away_team_name  = games[2].split(),games[3].split()

    print(home_team_name,away_team_name)

    def separation_home_away(team_, all_matches):
        home_matches = list()
        away_matches = list()
        for i in all_matches:
            x = i.index(team_[len(team_)-1])
            if i[x+1].isdigit():
                away_matches.append(i)
            elif "(" in i[x+1] and i[x+2].isdigit():
                away_matches.append(i)
            else:
                home_matches.append(i)
        return home_matches, away_matches

    team1_home, team1_away = separation_home_away(home_team_name, games[0])  # 1 team home / away matches
    team2_home, team2_away = separation_home_away(away_team_name, games[1])  # 2 team home / away matches





    for i in team2_home:
        print(i)
    for i in team2_away:
        print(i)
for i in schedule:
    main(i,b)
b.quit()