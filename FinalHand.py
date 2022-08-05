import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
url = "https://www.handball24.com/match/65cH7HcN/#/match-summary/match-summary"
try:
    browser = webdriver.Chrome()
    browser.get(url)
    browser.implicitly_wait(1)
    links = browser.find_elements(By.CSS_SELECTOR,"a.participant__participantName")
    class Participants:
        home_link = links[0].get_attribute("href")                                  # link to home team
        away_link = links[1].get_attribute("href")                                  # link to away team

    link = "{}/results/".format(Participants.home_link)
    team = link.split("/")[4].split("-")
    team_name_clear = ""

    browser.get(link)
    matches = browser.find_elements(By.CSS_SELECTOR,"[id^='g_7']")
    match_list,home_matches,away_matches = [],[],[]
    print(team[0].capitalize())
    for i in matches:                                                     # delete frendlies game
        if "(" in i.text or "Awrd" in i.text:
            continue
        match_list.append(i.text)
    for game in match_list:
        line = game.split()
        for j in line:
            if team[0].capitalize() in j or team[0].upper() in j :                          # get team name for searching
                team_name_clear = j
                break
        if len(line) < 8:                                                                   # delete cancelled matches
            continue
        if  line.index(team_name_clear) == 1 :      # separate home/away
            home_matches.append(line)
        elif (":" in line[1] or line[1]=="AET") and line.index(team_name_clear) == 2:
            home_matches.append(line)
        elif line[2] == "AET" and line.index(team_name_clear) == 3:
            home_matches.append(line)
        else:
            away_matches.append(line)
    home_first_half_ht, home_second_half_ht, away_second_half_ht, away_first_half_ht = [], [], [], []       # total halfs Home/Away Scored
    ft_home_ht, ft_away_ht = [], []
    handicap_home_first_half_ht,handicap_home_second_half_ht,handicap_home_fullfime_ht = [],[],[]
    home_first_half_conceded_ht, home_second_half_conceded_ht, away_first_half_conceded_ht, away_second_half_conceded_ht= [], [], [], []
    ft_home_conceded_ht, ft_away_conceded_ht = [], []

    for i in home_matches:                                                          # Scored start
        print(i)
        home_first_half_ht.append(int([j for j in i if j.isdigit()][2]))
        home_second_half_ht.append(int([j for j in i if j.isdigit()][4]))
    for i in range(len(home_second_half_ht)):
        ft_home_ht.append(int(home_first_half_ht[i]) + int(home_second_half_ht[i]))
    # print("*******************************************************************************")
    for i in away_matches:
        print(i)
        away_first_half_ht.append(int([j for j in i if j.isdigit()][3]))
        away_second_half_ht.append(int([j for j in i if j.isdigit()][5]))
    for i in range(len(away_first_half_ht)):
        ft_away_ht.append(int(away_first_half_ht[i]) + int(away_second_half_ht[i]))            # Scored end
    for i in home_matches:
        home_first_half_conceded_ht.append(int([j for j in i if j.isdigit()][3]))
        home_second_half_conceded_ht.append(int([j for j in i if j.isdigit()][5]))
    for i in range(len(home_first_half_conceded_ht)):
        ft_home_conceded_ht.append(int(home_first_half_conceded_ht[i]) + int(home_second_half_conceded_ht[i]))
    for i in away_matches:
        away_first_half_conceded_ht.append(int([j for j in i if j.isdigit()][2]))
        away_second_half_conceded_ht.append(int([j for j in i if j.isdigit()][4]))
    for i in range(len(away_second_half_conceded_ht)):
        ft_away_conceded_ht.append(int(away_first_half_conceded_ht[i]) + int(away_second_half_conceded_ht[i]))

    first_half_both_home_ht = [x + y for x, y in zip(home_first_half_ht, home_first_half_conceded_ht)]
    second_half_both_home_ht = [x + y for x, y in zip(home_second_half_ht,home_second_half_conceded_ht)]
    fulltime_home_ht = [x + y for x, y in zip(first_half_both_home_ht,second_half_both_home_ht)]
    ### HOME Scored home
    first_half_both_away_ht = [x + y for x, y in zip(away_first_half_ht,away_first_half_conceded_ht)]
    second_half_both_away_ht = [x + y for x, y in zip(away_second_half_ht,away_second_half_conceded_ht)]
    fulltime_away_ht = [x + y for x, y in zip(first_half_both_away_ht,second_half_both_away_ht)]
    ### HOME Scored away


    print("+"*30,"SCORED HOME","+"*30)
    print("1ST HALF:", sorted(home_first_half_ht))
    print("1 HALF BOTH: ", sorted(first_half_both_home_ht))
    print("2ND HALF:", sorted(home_second_half_ht))
    print("2 HALF BOTH: ", sorted(second_half_both_home_ht))
    print("FT:", sorted(ft_home_ht))
    print("FULL TIME: ", sorted(fulltime_home_ht))
    #######################################
    print("+"*30,"SCORED AWAY","+"*30)
    print("1ST HALF:", sorted(away_first_half_ht))
    print("1 HALF BOTH: ",sorted(first_half_both_away_ht))
    print("2ND HALF:", sorted(away_second_half_ht))
    print("2 HALF BOTH: ",sorted(second_half_both_away_ht))
    print("FT :", sorted(ft_away_ht))
    print("FULL TIME: ", sorted(fulltime_away_ht))
    #######################################
    print("-"*30,"CONCEDED HOME","-"*30)
    print("1ST HALF:", sorted(home_first_half_conceded_ht))
    print("2ND HALF:", sorted(home_second_half_conceded_ht))
    print("FT :", sorted(ft_home_conceded_ht))

    print("-"*30,"CONCEDED AWAY","-"*30)
    print("1ST HALF:", sorted(away_first_half_conceded_ht))
    print("2ND HALF:", sorted(away_second_half_conceded_ht))
    print("FT :", sorted(ft_away_conceded_ht))

    print()
    print("A++++++++++++++++++W+++++++++++++++++++++++++++A+++++++++++++++++++++++++++++Y")

    link = "{}/results/".format(Participants.away_link)
    team = link.split("/")[4].split("-")
    team_name_clear = ""
    browser.get(link)
    matches = browser.find_elements(By.CSS_SELECTOR,"[id^='g_7']")
    match_list,home_matches,away_matches = [],[],[]
    print(team[0].capitalize())
    for i in matches:                                                     # delete frendlies game
        if "(" in i.text or "Awrd" in i.text:
            continue
        match_list.append(i.text)
    for game in match_list:
        line = game.split()
        for j in line:
            if team[0].capitalize() in j or team[0].upper() in j :                          # get team name for searching
                team_name_clear = j
                break
        if len(line) < 8:                                                                   # delete cancelled matches
            continue
        if  line.index(team_name_clear) == 1 :      # separate home/away
            home_matches.append(line)
        elif (":" in line[1] or line[1]=="AET") and line.index(team_name_clear) == 2:
            home_matches.append(line)
        else:
            away_matches.append(line)
    home_first_half_at, home_second_half_at, away_second_half_at, away_first_half_at = [], [], [], []       # total halfs Home/Away Scored
    ft_home_at, ft_away_at = [], []
    handicap_home_first_half_at,handicap_home_second_half_at,handicap_home_fullfime_at = [],[],[]

    home_first_half_conceded_at, home_second_half_conceded_at, away_first_half_conceded_at, away_second_half_conceded_at= [], [], [], []
    ft_home_conceded_at, ft_away_conceded_at = [], []
    for i in home_matches:                                                          # Scored start
        print(i)
        home_first_half_at.append(int([j for j in i if j.isdigit()][2]))
        home_second_half_at.append(int([j for j in i if j.isdigit()][4]))
    for i in range(len(home_second_half_at)):
        ft_home_at.append(int(home_first_half_at[i]) + int(home_second_half_at[i]))
    # print("*******************************************************************************")
    for i in away_matches:
        print(i)
        away_first_half_at.append(int([j for j in i if j.isdigit()][3]))
        away_second_half_at.append(int([j for j in i if j.isdigit()][5]))
    for i in range(len(away_first_half_at)):
        ft_away_at.append(int(away_first_half_at[i]) + int(away_second_half_at[i]))            # Scored end
    for i in home_matches:
        home_first_half_conceded_at.append(int([j for j in i if j.isdigit()][3]))
        home_second_half_conceded_at.append(int([j for j in i if j.isdigit()][5]))
    for i in range(len(home_first_half_conceded_at)):
        ft_home_conceded_at.append(int(home_first_half_conceded_at[i]) + int(home_second_half_conceded_at[i]))
    for i in away_matches:
        away_first_half_conceded_at.append(int([j for j in i if j.isdigit()][2]))
        away_second_half_conceded_at.append(int([j for j in i if j.isdigit()][4]))
    for i in range(len(away_second_half_conceded_at)):
        ft_away_conceded_at.append(int(away_first_half_conceded_at[i]) + int(away_second_half_conceded_at[i]))

    first_half_both_home_at = [x + y for x, y in zip(home_first_half_at, home_first_half_conceded_at)]
    second_half_both_home_at = [x + y for x, y in zip(home_second_half_at,home_second_half_conceded_at)]
    fulltime_home_at = [x + y for x, y in zip(first_half_both_home_at,second_half_both_home_at)]
    ### AWAY Scored home
    first_half_both_away_at = [x + y for x, y in zip(away_first_half_at,away_first_half_conceded_at)]
    second_half_both_away_at = [x + y for x, y in zip(away_second_half_at,away_second_half_conceded_at)]
    fulltime_away_at = [x + y for x, y in zip(first_half_both_away_at,second_half_both_away_at)]
    ### AWAY Scored away


    print("+"*30,"SCORED HOME","+"*30)
    print("1ST HALF:", sorted(home_first_half_at))
    print("1 HALF BOTH: ", sorted(first_half_both_home_at))
    print("2ND HALF:", sorted(home_second_half_at))
    print("2 HALF BOTH: ", sorted(second_half_both_home_at))
    print("FT:", sorted(ft_home_at))
    print("FULL TIME: ", sorted(fulltime_home_at))
    #######################################
    print("+"*30,"SCORED AWAY","+"*30)
    print("1ST HALF:", sorted(away_first_half_at))
    print("1 HALF BOTH: ",sorted(first_half_both_away_at))
    print("2ND HALF:", sorted(away_second_half_at))
    print("2 HALF BOTH: ",sorted(second_half_both_away_at))
    print("FT :", sorted(ft_away_at))
    print("FULL TIME: ", sorted(fulltime_away_at))
    #######################################
    print("-"*30,"CONCEDED HOME","-"*30)
    print("1ST HALF:", sorted(home_first_half_conceded_at))
    print("2ND HALF:", sorted(home_second_half_conceded_at))
    print("FT :", sorted(ft_home_conceded_at))

    print("-"*30,"CONCEDED AWAY","-"*30)
    print("1ST HALF:", sorted(away_first_half_conceded_at))
    print("2ND HALF:", sorted(away_second_half_conceded_at))
    print("FT :", sorted(ft_away_conceded_at))
finally:
    browser.quit()