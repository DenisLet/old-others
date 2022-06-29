import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
link = "https://www.handball24.com/team/skanela/vV51VImP/results/{}".format("results/")
team = link.split("/")[4].split("-")
try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)
    browser.find_element(By.ID,"onetrust-reject-all-handler").click()
    matches = browser.find_elements(By.CSS_SELECTOR,"[id^='g_7']")
    match_list = []
    away_games,home_games,all_games = [],[],[]
    each_game = ""
    for i in matches:
        match_list.append(i.text)
    for game in match_list:
        line = game.split()
        each_game = ""
        for i in line:
            if "." in i or ":" in i or "AET" in i:
                continue
            if "Awrd" in i:
                break
            each_game += i + " "
        all_games.append(each_game)

    for i in list(filter(None, all_games)):
        if i.split()[0]==team[0].capitalize():
            home_games.append(i.split())
        else:
            away_games.append(i.split())
    print(*team)


finally:
    time.sleep(20)
    browser.quit()


