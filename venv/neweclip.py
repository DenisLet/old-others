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
        resume = input("Select matches and press enter to continue(Add to favorite) ")
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

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "eager"
b = webdriver.Chrome(desired_capabilities=caps)

def main(url,browser):
    try:
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
                if len([i for i in line.split() if i.isdigit() or "(" in i]) < 4:
                    continue
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
        team1_home,team1_away = separation_home_away(home_team_name,games[0])     # 1 team home / away matches
        team2_home,team2_away = separation_home_away(away_team_name,games[1])     # 2 team home / away matches
        # for i in team1_home:
        #     print(i)
        # for i in team1_away:
        #     print(i)
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
                if amount == 0:
                    return  1
                else:
                    return round(100 - (null / amount) * 100)
            return null, one, more, amount, percantage(null,one,more,amount)

        def first_half_results(matches, loc):
            team_scored = list()
            team_coceded = list()
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


        def first_half_personal(t1h,t1a,t2h,t2a,team1,team2,link):
            print(indication(team1_scored_fh_home),team1,"scored home")
            print(indication((team1)))
            pass

        def fulltime(matches,loc):
            team_scored = list()
            team_coceded = list()
            if loc == "home":
                scored, conceded = 0, 1
            else:
                scored, conceded = 1, 0
            for i in matches:
                scores = [j for j in i if j.isdigit() or j.isalnum() == False][-4:]
                if "(" in scores[0]:
                    scores[0], scores[1], scores[2], scores[3] = scores[2], scores[3], scores[0], scores[1]
                team_scored.append(int(scores[scored].replace("(", "").replace(")", "")))
                team_coceded.append(int(scores[conceded].replace("(", "").replace(")", "")))
            return team_scored, team_coceded  # 0 -scored 1 - conceded

        '''1st half individual collecting '''
        team1_scored_fh_home, team1_conceded_fh_home = first_half_results(team1_home,loc="home")
        team1_scored_fh_away, team1_conceded_fh_away = first_half_results(team1_away,loc="away")
        team2_scored_fh_home, team2_conceded_fh_home = first_half_results(team2_home,loc="home")
        team2_scored_fh_away, team2_conceded_fh_away = first_half_results(team2_away,loc="away")

        '''full time collecting individual  '''
        team1_scored_ft_home, team1_conceded_ft_home = fulltime(team1_home,loc="home")    # fh -> first half, ft -> full time
        team1_scored_ft_away, team1_conceded_ft_away = fulltime(team1_away,loc="away")
        team2_scored_ft_home, team2_conceded_ft_home = fulltime(team2_home,loc="home")
        team2_scored_ft_away, team2_conceded_ft_away = fulltime(team2_away,loc="away")


        '''full time collecting common '''
        team1_common_ft_home = [x + y for x, y in zip(team1_scored_ft_home, team1_conceded_ft_home)]
        team1_common_ft_away = [x + y for x, y in zip(team1_scored_ft_away, team1_conceded_ft_away)]
        team2_common_ft_home = [x + y for x, y in zip(team2_scored_ft_home, team2_conceded_ft_home)]
        team2_common_ft_away = [x + y for x, y in zip(team2_scored_ft_away, team2_conceded_ft_away)]


        '''second half individual collecting  '''
        team1_scored_sh_home = [x - y for x, y in zip(team1_scored_ft_home, team1_scored_fh_home)]
        team1_conceded_sh_home = [x - y for x, y in zip(team1_conceded_ft_home, team1_conceded_fh_home)]    # fh -> first half, ft -> full time, sh -> second half
        team1_scored_sh_away = [x - y for x, y in zip(team1_scored_ft_away, team1_scored_fh_away)]
        team1_conceded_sh_away = [x - y for x, y in zip(team1_conceded_ft_away, team1_conceded_fh_away)]
        team2_scored_sh_home = [x - y for x, y in zip(team2_scored_ft_home, team2_scored_fh_home)]
        team2_conceded_sh_home = [x - y for x, y in zip(team2_conceded_ft_home, team2_conceded_fh_home)]    # fh -> first half, ft -> full time, sh -> second half
        team2_scored_sh_away = [x - y for x, y in zip(team2_scored_ft_away, team2_scored_fh_away)]
        team2_conceded_sh_away = [x - y for x, y in zip(team2_conceded_ft_away, team2_conceded_fh_away)]

        '''second half common collecting '''
        team1_common_sh_home = [x + y for x, y in zip(team1_scored_sh_home, team1_conceded_sh_home)]
        team1_common_sh_away = [x + y for x, y in zip(team1_scored_sh_away, team1_conceded_sh_away)]
        team2_common_sh_home = [x + y for x, y in zip(team2_scored_sh_home, team2_conceded_sh_home)]
        team2_common_sh_away = [x + y for x, y in zip(team2_scored_sh_away, team2_conceded_sh_away)]


        '''1st half common collecting '''
        team1_common_fh_home = [x + y for x, y in zip(team1_scored_fh_home, team1_conceded_fh_home)]
        team1_common_fh_away = [x + y for x, y in zip(team1_scored_fh_away, team1_conceded_fh_away)]
        team2_common_fh_home = [x + y for x, y in zip(team2_scored_fh_home, team2_conceded_fh_home)]
        team2_common_fh_away = [x + y for x, y in zip(team2_scored_fh_away, team2_conceded_fh_away)]


        def first_half_bet(t1h,t1a,t2h,t2a,team1,team2,link):
            if indication(t1h)[4] + indication(t2a)[4] > 156:
                print(team1,indication(t1h),"scored home")
                print(team1, indication(t1a),"scored away")
                print(team2, indication(t2h),"scored home")
                print(team2, indication(t2a),"scored away")
                print(">1 Common %: ",round(indication(t1h)[4]+indication(t2a)[4])/2)
                print(link)


        # first_half_bet(team1_common_fh_home,team1_common_fh_away,team2_common_fh_home,team2_common_fh_away,home_team_name
        #               ,away_team_name,url)
        # print("1 HALF COMMON")
        # print(home_team_name, team1_common_fh_home,indication(team1_common_fh_home),"HOME")
        # print(home_team_name, team1_common_fh_away,indication(team1_common_fh_away),"AWAY")
        # print(away_team_name, team2_common_fh_home,indication(team2_common_fh_home),"HOME")
        # print(away_team_name, team2_common_fh_away,indication(team2_common_fh_away),"AWAY")
        # print("1 HALF SCORED")
        # print(home_team_name, team1_scored_fh_home,"RESULT(SCORED):",indication(team1_scored_fh_home))
        # print(away_team_name, team2_scored_fh_away,"RESULT(SCORED):",indication(team2_scored_fh_away))
        # print("1 HALF CONCEDED ")
        # print(home_team_name, team1_conceded_fh_home,"RESULT(CONCEDED)",indication(team1_conceded_fh_home))
        # print(away_team_name, team2_conceded_fh_away, "RESULT(CONCEDED)", indication(team2_conceded_fh_away))
        # print(indication(team1_common_fh_home))
        # print(indication(team1_common_fh_home)[4])

        if indication(team1_common_fh_home)[4] + indication(team2_common_fh_away)[4]>140:
            print("1 HALF COMMON")
            print(home_team_name, team1_common_fh_home, indication(team1_common_fh_home), "HOME")
            print(home_team_name, team1_common_fh_away, indication(team1_common_fh_away), "AWAY")
            print(away_team_name, team2_common_fh_home, indication(team2_common_fh_home), "HOME")
            print(away_team_name, team2_common_fh_away, indication(team2_common_fh_away), "AWAY")
            print("1 HALF SCORED")
            print(home_team_name, team1_scored_fh_home, "RESULT(SCORED):", indication(team1_scored_fh_home))
            print(away_team_name, team2_scored_fh_away, "RESULT(SCORED):", indication(team2_scored_fh_away))
            print("1 HALF CONCEDED ")
            print(home_team_name, team1_conceded_fh_home, "RESULT(CONCEDED)", indication(team1_conceded_fh_home))
            print(away_team_name, team2_conceded_fh_away, "RESULT(CONCEDED)", indication(team2_conceded_fh_away))
            print(url)
        if indication(team1_common_ft_home)[4] + indication(team2_common_ft_away)[4] > 150:
            print("FULLTIME")
            print(home_team_name, team1_common_ft_home, indication(team1_common_ft_home), "HOME")
            print(home_team_name, team1_common_ft_away, indication(team1_common_ft_away), "AWAY")
            print(away_team_name, team2_common_ft_home, indication(team2_common_ft_home), "HOME")
            print(away_team_name, team2_common_ft_away, indication(team2_common_ft_away), "AWAY")
            print("FULLTIME SCORED")
            print(home_team_name, team1_scored_ft_home,"RESULT(SCORED):",indication(team1_scored_ft_home))
            print(away_team_name, team2_scored_ft_away,"RESULT(SCORED):",indication(team2_scored_ft_away))
            print("FULLTIME CONCEDED ")
            print(home_team_name, team1_conceded_ft_home,"RESULT(CONCEDED)",indication(team1_conceded_ft_home))
            print(away_team_name, team2_conceded_ft_away, "RESULT(CONCEDED)", indication(team2_conceded_ft_away))
            print(url)
        if  indication(team1_common_sh_home)[4] + indication(team2_common_sh_away)[4] > 1140:
            print("2 HALF COMMON")
            print(home_team_name, team1_common_sh_home,indication(team1_common_sh_home),"HOME")
            print(home_team_name, team1_common_sh_away,indication(team1_common_sh_away),"AWAY")
            print(away_team_name, team2_common_sh_home,indication(team2_common_sh_home),"HOME")
            print(away_team_name, team2_common_sh_away,indication(team2_common_sh_away),"AWAY")
            print("2 HALF SCORED")
            print(home_team_name, team1_scored_sh_home,"RESULT(SCORED):",indication(team1_scored_sh_home))
            print(away_team_name, team2_scored_sh_away,"RESULT(SCORED):",indication(team2_scored_sh_away))
            print("2 HALF CONCEDED ")
            print(home_team_name, team1_conceded_sh_home,"RESULT(CONCEDED)",indication(team1_conceded_sh_home))
            print(away_team_name, team2_conceded_sh_away, "RESULT(CONCEDED)", indication(team2_conceded_sh_away))
            print(url)
        if (indication(team1_scored_ft_home)[4] > 85 and indication(team2_conceded_ft_away)[4] > 85)\
                or (indication(team1_conceded_ft_home)[4] > 85 and indication(team2_scored_ft_away)[4] > 85):
            print("FULLTIME SCORED")
            print(home_team_name, team1_scored_ft_home,"RESULT(SCORED):",indication(team1_scored_ft_home))
            print(away_team_name, team2_scored_ft_away,"RESULT(SCORED):",indication(team2_scored_ft_away))
            print("FULLTIME CONCEDED ")
            print(home_team_name, team1_conceded_ft_home,"RESULT(CONCEDED)",indication(team1_conceded_ft_home))
            print(away_team_name, team2_conceded_ft_away, "RESULT(CONCEDED)", indication(team2_conceded_ft_away))
            print(url)
    finally:
        print(time.time() - start)
        #browser.quit()
for i in schedule:
    main(i,b)
