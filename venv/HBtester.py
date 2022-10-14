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

    def separator(matches):
        match_list = list()
        for i in matches:
            line = i.text
            if "(" in line or "Awrd" in line:
                continue
            if len([i for i in line.split() if i.isdigit()]) < 6:
                continue
            match_list.append(line.split())
        return match_list

    def forming(browser, link1, link2):  # NEED ADD TYPE SPORT AND FIXABLE CSS SELECTOR
        browser.get(link1)
        matches = browser.find_elements(By.CSS_SELECTOR, "[id^='g_7']")
        match_list_home = separator(matches)
        browser.get(link2)
        matches = browser.find_elements(By.CSS_SELECTOR, "[id^='g_7']")
        match_list_away = separator(matches)
        return match_list_home, match_list_away

    games = forming(browser, team_home, team_away)


    def team_name(list1, list2):
        if len(list1) > 0:
            team1 = set(reduce(lambda i, j: i & j, (set(x) for x in list1)))
        else:
            team1 = ""
        if len(list2) > 0:
            team2 = set(reduce(lambda i, j: i & j, (set(x) for x in list2)))
        else:
            team2 = ""
        return team1, team2

    home_team_name, away_team_name = team_name(games[0], games[1])

    def separation_home_away(team_, all_matches):
        home_matches = list()
        away_matches = list()
        for i in all_matches:
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

    team1_home, team1_away = separation_home_away(home_team_name, games[0])  # 1 team home / away matches
    team2_home, team2_away = separation_home_away(away_team_name, games[1])  # 2 team home / away matches


    def results_first_half(matches,team,loc):
        count=0
        for i in team:
            print(i)
            if i.isdigit():
                count+=1
        team_scored = []
        team_conceded = []
        if loc == "home":
            scored, conceded = 2 + count, 3 + count
        else:
            scored, conceded = 3 + count, 2 + count
        for i in matches:
            scores = [j for j in i if j.isdigit()]
            team_scored.append(int(scores[scored]))
            team_conceded.append(int(scores[conceded]))
        return team_scored,team_conceded

    def results_second_half(matches,team, loc):
        count=0
        for i in team:
            if i.isdigit():
                count+=1
        team_scored = list()
        team_coceded = list()
        if loc == "home":
            scored,conceded = 4 + count, 5 + count
        else:
            scored,conceded = 5 + count, 4 + count
        for i in matches:
            scores = [j for j in i if j.isdigit()]
            team_scored.append(int(scores[scored]))
            team_coceded.append(int(scores[conceded]))
        return team_scored, team_coceded  # 4 -scored 5 - conceded

    def fulltime(home,away):
        return [x + y for x, y in zip(home, away)]

    ''' 1st half results individual '''

    team1_scored_fh_home, team1_conceded_fh_home = results_first_half(team1_home,home_team_name, loc="home")
    team1_scored_fh_away, team1_conceded_fh_away = results_first_half(team1_away,home_team_name, loc="away")
    team2_scored_fh_home, team2_conceded_fh_home = results_first_half(team2_home,away_team_name, loc="home")
    team2_scored_fh_away, team2_conceded_fh_away = results_first_half(team2_away,away_team_name, loc="away")

    ''' second half results individual'''

    team1_scored_sh_home, team1_conceded_sh_home = results_second_half(team1_home,home_team_name, loc="home")
    team1_scored_sh_away, team1_conceded_sh_away = results_second_half(team1_away,home_team_name, loc="away")
    team2_scored_sh_home, team2_conceded_sh_home = results_second_half(team2_home,away_team_name, loc="home")
    team2_scored_sh_away, team2_conceded_sh_away = results_second_half(team2_away,away_team_name, loc="away")

    '''teams fulltime indinvidual'''

    team1_ft_home_scored = fulltime(team1_scored_fh_home,team1_scored_sh_home)
    team1_ft_away_scored = fulltime(team1_scored_fh_away, team1_scored_sh_away)
    team2_ft_home_scored = fulltime(team2_scored_fh_home,team2_scored_sh_home)
    team2_ft_away_scored = fulltime(team2_scored_fh_away, team2_scored_sh_away)
    team1_ft_home_conceded = fulltime(team1_conceded_fh_home,team1_conceded_sh_home)
    team1_ft_away_conceded = fulltime(team1_conceded_fh_away, team1_conceded_sh_away)
    team2_ft_home_conceded = fulltime(team2_conceded_fh_home,team2_conceded_sh_home)
    team2_ft_away_conceded = fulltime(team2_conceded_fh_away, team2_conceded_sh_away)

    '''1st half common'''

    team1_common_fh_home = fulltime(team1_scored_fh_home,team1_conceded_fh_home)
    team1_common_fh_away = fulltime(team1_scored_fh_away,team1_conceded_fh_away)
    team2_common_fh_home = fulltime(team2_scored_fh_home,team2_conceded_fh_home)
    team2_common_fh_away = fulltime(team2_scored_fh_away,team2_conceded_fh_away)

    '''2nd half common'''

    team1_common_sh_home = fulltime(team1_scored_sh_home,team1_conceded_sh_home)
    team1_common_sh_away = fulltime(team1_scored_sh_away,team1_conceded_sh_away)
    team2_common_sh_home = fulltime(team2_scored_sh_home,team2_conceded_sh_home)
    team2_common_sh_away = fulltime(team2_scored_sh_away,team2_conceded_sh_away)

    '''fulltime common'''

    team1_common_ft_home = fulltime(team1_ft_home_scored,team1_ft_home_conceded)
    team1_common_ft_away = fulltime(team1_ft_away_scored,team1_ft_away_conceded)
    team2_common_ft_home = fulltime(team2_ft_home_scored,team2_ft_home_conceded)
    team2_common_ft_away = fulltime(team2_ft_away_scored,team2_ft_away_conceded)


    print("+"*30,"SCORED HOME","+"*30)
    print(" " * 27, home_team_name)
    print("1ST HALF   :", (team1_scored_fh_home))
    print("1 HALF BOTH:", (team1_common_fh_home))
    print("2ND HALF   :", (team1_scored_sh_home))
    print("2 HALF BOTH:", (team1_common_sh_home))
    print("FT  IND    :", (team1_ft_home_scored))
    print("FULL TIME  :", (team1_common_ft_home))
    ######################################
    print("+"*30,"SCORED AWAY","+"*30)
    print("1ST HALF   :", (team1_scored_fh_away))
    print("1 HALF BOTH:", (team1_common_fh_away))
    print("2ND HALF   :", (team1_scored_sh_away))
    print("2 HALF BOTH:", (team1_common_sh_away))
    print("FT  IND    :", (team1_ft_away_scored))
    print("FULL TIME  :", (team1_common_ft_away))
    #######################################
    print("-"*30,"CONCEDED HOME","-"*30)
    print("1ST HALF   :", (team1_conceded_fh_home))
    print("2ND HALF   :", (team1_conceded_sh_home))
    print("FT  IND    :", (team1_ft_home_conceded))
    #######################################
    print("-"*30,"CONCEDED AWAY","-"*30)
    print("1ST HALF   :", (team1_conceded_fh_away))
    print("2ND HALF   :", (team1_conceded_sh_away))
    print("FT  IND    :", (team1_ft_away_conceded))
    #######################################
    print()
    print("+"*30,"SCORED HOME","+"*30)
    print(" " * 27, away_team_name)
    print("1ST HALF   :", (team2_scored_fh_home))
    print("1 HALF BOTH:", (team2_common_fh_home))
    print("2ND HALF   :", (team2_scored_sh_home))
    print("2 HALF BOTH:", (team2_common_sh_home))
    print("FT  IND    :", (team2_ft_home_scored))
    print("FULL TIME  :", (team2_common_ft_home))
    ######################################
    print("+"*30,"SCORED AWAY","+"*30)
    print("1ST HALF   :", (team2_scored_fh_away))
    print("1 HALF BOTH:", (team2_common_fh_away))
    print("2ND HALF   :", (team2_scored_sh_away))
    print("2 HALF BOTH:", (team2_common_sh_away))
    print("FT  IND    :", (team2_ft_away_scored))
    print("FULL TIME  :", (team2_common_ft_away))
    #######################################
    print("-"*30,"CONCEDED HOME","-"*30)
    print("1ST HALF   :", (team2_conceded_fh_home))
    print("2ND HALF   :", (team2_conceded_sh_home))
    print("FT  IND    :", (team2_ft_home_conceded))
    #######################################
    print("-"*30,"CONCEDED AWAY","-"*30)
    print("1ST HALF   :", (team2_conceded_fh_away))
    print("2ND HALF   :", (team2_conceded_sh_away))
    print("FT  IND    :", (team2_ft_away_conceded))



for i in schedule:
    main(i,b)
b.quit()

