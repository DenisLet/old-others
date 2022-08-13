from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from functools import reduce
import time
start = time.time()
def creation():
    try:
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
    finally:
        browser.quit()
    return checklist

schedule = creation()

def main(url):
    try:
        caps = DesiredCapabilities().CHROME
        caps["pageLoadStrategy"] = "eager"
        browser = webdriver.Chrome(desired_capabilities=caps)
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
                if "Awrd" in line:
                    continue
                if "(0)" in line or "(1)" in line or "(2)" in line or "(3)" in line:
                    match_list.append(line.split())
            return match_list
        def forming(browser, link1,link2):  # NEED ADD TYPE SPORT AND FIXABLE CSS SELECTOR
            browser.get(link1)
            matches = browser.find_elements(By.CSS_SELECTOR,"[id^='g_1']")
            match_list_home = separator(matches)
            browser.get(link2)
            matches = browser.find_elements(By.CSS_SELECTOR,"[id^='g_1']")
            match_list_away = separator(matches)
            return match_list_home,match_list_away
        games = forming(browser, team_home, team_away)
        def team_name(list1,list2):
            if len(list1) > 0:
                team1= set(reduce(lambda i, j: i & j, (set(x) for x in list1)))
            else:
                team1 = ""
            if len(list2) > 0:
                team2 = set(reduce(lambda i, j: i & j, (set(x) for x in list2)))
            else:
                team2 = ""
            return team1,team2
        home_team_name, away_team_name = team_name(games[0],games[1])
        print(home_team_name,away_team_name)
        def separation_home_away(team_, all_matches):
            count = 0
            home_matches = list()
            away_matches = list()
            for i in all_matches:
                count += 1
                if len(team_) == 1:
                    if i[1] in team_:
                        home_matches.append(i)
                    elif i[2] in team_ and ":" in i[1]:
                        home_matches.append(i)
                    elif (i[1] == "AET" or i[2] == "AET" or i[1] == "Pen" or i[2] == "Pen") and i[3] in team_:
                        home_matches.append(i)
                    else:
                        away_matches.append(i)
                else:
                    if i[1] in team_ and i[2] in team_:
                        home_matches.append(i)
                    elif i[2] in team_ and i[3] in team_ and ":" in i[1]:
                        home_matches.append(i)
                    elif (i[1] == "AET" or i[2] == "AET" or i[1] == "Pen" or i[2] == "Pen") and i[3] in team_ and i[
                        4] in team_:
                        home_matches.append(i)
                    else:
                        away_matches.append(i)
            return home_matches, away_matches
        team1_home,team1_away = separation_home_away(home_team_name,games[0])
        team2_home,team2_away = separation_home_away(away_team_name,games[1])
        for i in team1_home:
            print(i)
        for i in team1_away:
            print(i)
        def indication(list):
            null, one, more, amount = 0, 0, 0, 0
            for i in list:
                amount += 1
                if i == 0:
                    null += 1
                if i == 1:
                    one += 1
                if i > 1:
                    more += 1
            def percantage(null,one,more,amount):
                return round(100 - (null / amount) * 100)
            return null, one, more, amount, percantage(null,one,more,amount)

        def first_half_results(matches, loc):
            team_scored = list()
            team_coceded = list()
            total_half = list()
            if loc == "home":
                scored, conceded = 2, 3
            else:
                scored, conceded = 3, 2
            for i in matches:
                scores = [j for j in i if j.isdigit() or j.isalnum() == False][-4:]
                if "(" in scores[0]:
                    scores[0], scores[1], scores[2], scores[3] = scores[2], scores[3], scores[0], scores[1]
                team_scored.append(int(scores[scored].replace("(", "").replace(")", "")))
                team_coceded.append(int(scores[conceded].replace("(", "").replace(")", "")))
            return team_scored, team_coceded  # 0 -scored 1 - conceded
        team1_scored_fh_home, team1_conceded_fh_home = first_half_results(team1_home,loc="home")
        team1_scored_fh_away, team1_conceded_fh_away = first_half_results(team1_away,loc="away")
        team2_scored_fh_home, team2_conceded_fh_home = first_half_results(team2_home,loc="home")
        team2_scored_fh_away, team2_conceded_fh_away = first_half_results(team2_away,loc="away")
        team1_common_fh_home = [x + y for x, y in zip(team1_scored_fh_home, team1_conceded_fh_home)]
        team1_common_fh_away = [x + y for x, y in zip(team1_scored_fh_away, team1_conceded_fh_away)]
        team2_common_fh_home = [x + y for x, y in zip(team2_scored_fh_home, team2_conceded_fh_home)]
        team2_common_fh_away = [x + y for x, y in zip(team2_scored_fh_away, team2_conceded_fh_away)]
        print(home_team_name, team1_common_fh_home,indication(team1_common_fh_home),"HOME")
        print(home_team_name, team1_common_fh_away,indication(team1_common_fh_away),"AWAY")
        print(away_team_name, team2_common_fh_home,indication(team2_common_fh_home),"HOME")
        print(away_team_name, team2_common_fh_away,indication(team2_common_fh_away),"AWAY")
        print()
        print(home_team_name, team1_scored_fh_home,"RESULT(SCORED):",indication(team1_scored_fh_home))
        print(away_team_name, team2_scored_fh_away,"RESULT(SCORED):",indication(team2_scored_fh_away))
        print()
        print(home_team_name, team1_conceded_fh_home,"RESULT(CONCEDED)",indication(team1_conceded_fh_home))
        print(away_team_name, team2_conceded_fh_away, "RESULT(CONCEDED)", indication(team2_conceded_fh_away))
        if indication(team1_common_fh_home)[4] + indication(team2_common_fh_away)[4] > 150:
            print(url)
    finally:
        print(time.time() - start)
        browser.quit()

for i in schedule:
    main(i)