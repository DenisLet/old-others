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
            #  print(line)
            if "(" in line or "Awrd" in line:
                continue
            if len([i for i in line.split() if i.isdigit()]) < 6:
                continue
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

    home_team_name, away_team_name  = games[2].split(), games[3].split()

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


    for i in team1_home:
        print(i)
    for i in team1_away:
        print(i)


    for i in team2_home:
        print(i)
    for i in team2_away:
        print(i)

    def results(matches,loc,period):
        if period == "first":
            x,y = 2,3
        if period == "second":
            x,y = 4,5
        if period == "third":
            x,y = 6,7
        team_scored = []
        team_conceded = []
        if loc == "home":
            scored, conceded = x , y
        else:
            scored, conceded = y , x
        for i in matches:
            if 'Pen' in i:
                scores = i[-13:-1]
            elif "AOT" in i:
                scores = i[-11:-1]
            else:
                scores = i[-9:-1]

            team_scored.append(int(scores[scored]))
            team_conceded.append(int(scores[conceded]))

        return team_scored,team_conceded

    ''' 1st period results individual '''

    team1_scored_1p_home, team1_conceded_1p_home = results(team1_home, loc="home",period="first")
    team1_scored_1p_away, team1_conceded_1p_away = results(team1_away, loc="away",period="first")
    team2_scored_1p_home, team2_conceded_1p_home = results(team2_home, loc="home",period="first")
    team2_scored_1p_away, team2_conceded_1p_away = results(team2_away, loc="away",period="first")

    '''2nd period results individual'''

    team1_scored_2p_home, team1_conceded_2p_home = results(team1_home, loc="home",period="second")
    team1_scored_2p_away, team1_conceded_2p_away = results(team1_away, loc="away",period="second")
    team2_scored_2p_home, team2_conceded_2p_home = results(team2_home, loc="home",period="second")
    team2_scored_2p_away, team2_conceded_2p_away = results(team2_away, loc="away",period="second")

    '''3rd period results individual'''

    team1_scored_3p_home, team1_conceded_3p_home = results(team1_home, loc="home",period="third")
    team1_scored_3p_away, team1_conceded_3p_away = results(team1_away, loc="away",period="third")
    team2_scored_3p_home, team2_conceded_3p_home = results(team2_home, loc="home",period="third")
    team2_scored_3p_away, team2_conceded_3p_away = results(team2_away, loc="away",period="third")

    '''Fulltime results individual'''

    def fulltime(period1,period2,period3):
        return [int(x) +int(y)+ int(z) for x, y, z in zip(period1,period2,period3)]


    team1_scored_ft_home = fulltime(team1_scored_1p_home,team1_scored_2p_home,team1_scored_3p_home)
    team1_scored_ft_away = fulltime(team1_scored_1p_away,team1_scored_2p_away,team1_scored_3p_away)
    team1_conceded_ft_home = fulltime(team1_conceded_1p_home,team1_conceded_2p_home,team1_conceded_3p_home)
    team1_conceded_ft_away = fulltime(team1_conceded_1p_away,team1_conceded_2p_away,team1_conceded_3p_away)
    team2_scored_ft_home = fulltime(team2_scored_1p_home,team2_scored_2p_home,team2_scored_3p_home)
    team2_scored_ft_away = fulltime(team2_scored_1p_away,team2_scored_2p_away,team2_scored_3p_away)
    team2_conceded_ft_home = fulltime(team2_conceded_1p_home,team2_conceded_2p_home,team2_conceded_3p_home)
    team2_conceded_ft_away = fulltime(team2_conceded_1p_away,team2_conceded_2p_away,team2_conceded_3p_away)

    '''Fulltime results common'''

    team1_common_ft_home = [x + y for x, y in zip(team1_scored_ft_home, team1_conceded_ft_home)]
    team1_common_ft_away = [x + y for x, y in zip(team1_scored_ft_away, team1_conceded_ft_away)]
    team2_common_ft_home = [x + y for x, y in zip(team2_scored_ft_home, team2_conceded_ft_home)]
    team2_common_ft_away = [x + y for x, y in zip(team2_scored_ft_away, team2_conceded_ft_away)]

    '''1st period common result'''

    team1_common_1p_home = [x + y for x, y in zip(team1_scored_1p_home, team1_conceded_1p_home)]
    team1_common_1p_away = [x + y for x, y in zip(team1_scored_1p_away, team1_conceded_1p_away)]
    team2_common_1p_home = [x + y for x, y in zip(team2_scored_1p_home, team2_conceded_1p_home)]
    team2_common_1p_away = [x + y for x, y in zip(team2_scored_1p_away, team2_conceded_1p_away)]

    '''2nd period common result'''

    team1_common_2p_home = [x + y for x, y in zip(team1_scored_2p_home, team1_conceded_2p_home)]
    team1_common_2p_away = [x + y for x, y in zip(team1_scored_2p_away, team1_conceded_2p_away)]
    team2_common_2p_home = [x + y for x, y in zip(team2_scored_2p_home, team2_conceded_2p_home)]
    team2_common_2p_away = [x + y for x, y in zip(team2_scored_2p_away, team2_conceded_2p_away)]



    '''3rd period common result'''

    team1_common_3p_home = [x + y for x, y in zip(team1_scored_3p_home, team1_conceded_3p_home)]
    team1_common_3p_away = [x + y for x, y in zip(team1_scored_3p_away, team1_conceded_3p_away)]
    team2_common_3p_home = [x + y for x, y in zip(team2_scored_3p_home, team2_conceded_3p_home)]
    team2_common_3p_away = [x + y for x, y in zip(team2_scored_3p_away, team2_conceded_3p_away)]

    '''Total calculation'''

    def calc(list):
        matches = 0
        zero, one, two, three, four, more = 0, 0, 0, 0, 0, 0
        for i in list:
            matches += 1
            if int(i) == 0:
                zero += 1
            elif int(i) == 1:
                one += 1
            elif int(i) == 2:
                two += 1
            elif int(i) == 3:
                three += 1
            elif int(i) == 4:
                four += 1
            else:
                more += 1
        return zero, one, two, three, four, more, matches




    '''Printer'''

    print("<<<<<HOME TEAM RESULTS>>>>>", home_team_name)
    print("<<<<<    1ST PERIOD   >>>>>")
    print("1ST PERIOD SCORED  HOME: ",team1_scored_1p_home,calc(team1_scored_1p_home))
    print("1ST PERIOD CONCED. HOME: ",team1_conceded_1p_home,calc(team1_conceded_1p_home))
    print("1ST PERIOD SCORED  AWAY: ",team1_scored_1p_away,calc(team1_scored_1p_away))
    print("1ST PERIOD CONCED. AWAY: ",team1_conceded_1p_away,calc(team1_conceded_1p_away))
    print("1ST PERIOD COMMON HOME : ",team1_common_1p_home,calc(team1_common_1p_home))
    print("1ST PERIOD COMMON AWAY : ",team1_common_1p_away,calc(team1_common_1p_away))
    print("<<<<<    2ND PERIOD   >>>>>")
    print("2ND PERIOD SCORED  HOME: ",team1_scored_2p_home,calc(team1_scored_2p_home))
    print("2ND PERIOD CONCED. HOME: ",team1_conceded_2p_home,calc(team1_conceded_2p_home))
    print("2ND PERIOD SCORED  AWAY: ",team1_scored_2p_away,calc(team1_scored_2p_away))
    print("2ND PERIOD CONCED. AWAY: ",team1_conceded_2p_away,calc(team1_conceded_2p_away))
    print("2ND PERIOD COMMON HOME : ",team1_common_2p_home,calc(team1_common_2p_home))
    print("2ND PERIOD COMMON AWAY : ",team1_common_2p_away,calc(team1_common_2p_away))
    print("<<<<<    3RD PERIOD   >>>>>")
    print("3RD PERIOD SCORED  HOME: ",team1_scored_3p_home,calc(team1_scored_3p_home))
    print("3RD PERIOD CONCED. HOME: ",team1_conceded_3p_home,calc(team1_conceded_3p_home))
    print("3RD PERIOD SCORED  AWAY: ",team1_scored_3p_away,calc(team1_scored_3p_away))
    print("3RD PERIOD CONCED. AWAY: ",team1_conceded_3p_away,calc(team1_conceded_3p_away))
    print("3RD PERIOD COMMON HOME : ",team1_common_3p_home,calc(team1_common_3p_home))
    print("3RD PERIOD COMMON AWAY : ",team1_common_3p_away,calc(team1_common_3p_away))
    print("<<<<<    FULLTIME   >>>>>")
    print("SCORED   FULLTIME  HOME: ",team1_scored_ft_home,calc(team1_scored_ft_home))
    print("CONCEDED FULLTIME  HOME: ",team1_conceded_ft_home,calc(team1_conceded_ft_home))
    print("SCORED   FULLTIME  AWAY: ",team1_scored_ft_away,calc(team1_scored_ft_away))
    print("CONCEDED FULLTIME  AWAY: ",team1_conceded_ft_away,calc(team1_conceded_ft_away))
    print("SCORED    COMMON   HOME: ",team1_common_ft_home,calc(team1_common_ft_home) )
    print("SCORED    COMMON   AWAY: ",team1_common_ft_away,calc(team1_common_ft_away) )
    print("*"*40)
    print("<<<<<AWAY TEAM RESULTS>>>>>", away_team_name)
    print("<<<<<    1ST PERIOD   >>>>>")
    print("1ST PERIOD SCORED  HOME: ", team2_scored_1p_home,calc(team2_scored_1p_home))
    print("1ST PERIOD CONCED. HOME: ", team2_conceded_1p_home,calc(team2_conceded_1p_home))
    print("1ST PERIOD SCORED  AWAY: ", team2_scored_1p_away,calc(team2_scored_1p_away))
    print("1ST PERIOD CONCED. AWAY: ", team2_conceded_1p_away,calc(team2_conceded_1p_away))
    print("1ST PERIOD COMMON HOME : ", team2_common_1p_home,calc(team2_common_1p_home))
    print("1ST PERIOD COMMON AWAY : ", team2_common_1p_away,calc(team2_common_1p_away))
    print("<<<<<    2ND PERIOD   >>>>>")
    print("2ND PERIOD SCORED  HOME: ", team2_scored_2p_home,calc(team2_scored_2p_home))
    print("2ND PERIOD CONCED. HOME: ", team2_conceded_2p_home,calc(team2_conceded_2p_home))
    print("2ND PERIOD SCORED  AWAY: ", team2_scored_2p_away,calc(team2_scored_2p_away))
    print("2ND PERIOD CONCED. AWAY: ", team2_conceded_2p_away,calc(team2_conceded_2p_away))
    print("2ND PERIOD COMMON HOME : ", team2_common_2p_home,calc(team2_common_2p_home))
    print("2ND PERIOD COMMON AWAY : ", team2_common_2p_away,calc(team2_common_2p_away))
    print("<<<<<    3RD PERIOD   >>>>>")
    print("3RD PERIOD SCORED  HOME: ", team2_scored_3p_home,calc(team2_scored_3p_home))
    print("3RD PERIOD CONCED. HOME: ", team2_conceded_3p_home,calc(team2_conceded_3p_home))
    print("3RD PERIOD SCORED  AWAY: ", team2_scored_3p_away,calc(team2_scored_3p_away))
    print("3RD PERIOD CONCED. AWAY: ", team2_conceded_3p_away,calc(team2_conceded_3p_away))
    print("3RD PERIOD COMMON HOME : ", team2_common_3p_home,calc(team2_common_3p_home))
    print("3RD PERIOD COMMON AWAY : ", team2_common_3p_away,calc(team2_common_3p_away))
    print("<<<<<    FULLTIME   >>>>>")
    print("SCORED   FULLTIME  HOME: ", team2_scored_ft_home,calc(team2_scored_ft_home))
    print("CONCEDED FULLTIME  HOME: ", team2_conceded_ft_home,calc(team2_conceded_ft_home))
    print("SCORED   FULLTIME  AWAY: ", team2_scored_ft_away,calc(team2_scored_ft_away))
    print("CONCEDED FULLTIME  AWAY: ", team2_conceded_ft_away,calc(team2_conceded_ft_away))
    print("SCORED    COMMON   HOME: ", team2_common_ft_home,calc(team2_common_ft_home))
    print("SCORED    COMMON   AWAY: ", team2_common_ft_away,calc(team2_common_ft_away))

for i in schedule:
    main(i,b)
b.quit()