import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
link = "https://www.handball24.com/team/sc-magdeburg/t8qpYkr1/{}".format("results/")
team = link.split("/")[4].split("-")
team_name_clear = ""
try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)
    browser.find_element(By.ID,"onetrust-reject-all-handler").click()
    matches = browser.find_elements(By.CSS_SELECTOR,"[id^='g_7']")
    match_list,home_matches,away_matches = [],[],[]
    print(team[0].capitalize())
    for i in matches:                                                     # delete frendlies game
        if "(" in i.text or "Awrd" in i.text:
            continue
        match_list.append(i.text)
    for i in match_list:                                                  # get team name for searching
        line = i.split()
        for j in line:
            if team[0].capitalize() in j:
                team_name_clear = j
                break
    print(team_name_clear)
    # for i in match_list:
    #     print(i.split())
    for game in match_list:
        line = game.split()
        if len(line) < 8:
            continue
        if line[line.index("{}".format(team_name_clear))+1].isdigit():                 # searching for team_name_clear
            away_matches.append(line)
        else:
            home_matches.append(line)

    for u in home_matches:
        print(u)





finally:
    time.sleep(20)
    browser.quit()