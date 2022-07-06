import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
link = "https://www.handball24.com/team/flensburg-h/G6mqiEzL/{}".format("results/")
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
    for game in match_list:
        line = game.split()
        print(line)
        for j in line:
            if team[0].capitalize() in j or team[0].upper() in j :                          # get team name for searching
                team_name_clear = j
                break
        print(team_name_clear)
        if len(line) < 8:                                                                   # delete cancelled matches
            continue
        if  line.index(team_name_clear) == 1 :      # separate home/away
            home_matches.append(line)
        elif ":" in line[1] and line.index(team_name_clear) == 2:
            home_matches.append(line)
        else:
            away_matches.append(line)
    home_first_half,home_second_half,away_second_half,away_first_half = [],[],[],[]       # total halfs Home/Away Scored
    ft_home,ft_away = [],[]
    home_first_half_conceded,home_second_half_conceded,away_first_half_conceded,away_second_half_conceded=[],[],[],[]
    ft_home_conceded,ft_away_conceded = [],[]
    for i in home_matches:                                                          # Scored start
        print(i)
        home_first_half.append(int([j for j in i if j.isdigit()][2]))
        home_second_half.append(int([j for j in i if j.isdigit()][4]))
    for i in range(len(home_second_half)):
        ft_home.append(int(home_first_half[i])+int(home_second_half[i]))
    print("*******************************************************************************")
    for i in away_matches:
        print(i)
        away_first_half.append(int([j for j in i if j.isdigit()][3]))
        away_second_half.append(int([j for j in i if j.isdigit()][5]))
    for i in range(len(away_first_half)):
        ft_away.append(int(away_first_half[i])+int(away_second_half[i]))            # Scored end
    for i in home_matches:
        home_first_half_conceded.append(int([j for j in i if j.isdigit()][3]))
        home_second_half_conceded.append(int([j for j in i if j.isdigit()][5]))
    for i in range(len(home_first_half_conceded)):
        ft_home_conceded.append(int(home_first_half_conceded[i])+int(home_second_half_conceded[i]))
    for i in away_matches:
        away_first_half_conceded.append(int([j for j in i if j.isdigit()][2]))
        away_second_half_conceded.append(int([j for j in i if j.isdigit()][4]))
    for i in range(len(away_second_half_conceded)):
        ft_away_conceded.append(int(away_first_half_conceded[i])+int(away_second_half_conceded[i]))
    print("+"*30,"SCORED HOME","+"*30)
    print("1ST HALF:",sorted(home_first_half))
    print("2ND HALF:",sorted(home_second_half))
    print("FH :",sorted(ft_home))
    print("+"*30,"SCORED AWAY","+"*30)
    print("1ST HALF:",sorted(away_first_half))
    print("2ND HALF:",sorted(away_second_half))
    print("FH :",sorted(ft_away))
    print("-"*30,"CONCEDED HOME","-"*30)
    print("1ST HALF:",sorted(home_first_half_conceded))
    print("2ND HALF:",sorted(home_second_half_conceded))
    print("FH :",sorted(ft_home_conceded))
    print("-"*30,"CONCEDED AWAY","-"*30)
    print("1ST HALF:",sorted(away_first_half_conceded))
    print("2ND HALF:",sorted(away_second_half_conceded))
    print("FH :",sorted(ft_away_conceded))

finally:
    time.sleep(20)
    browser.quit()


