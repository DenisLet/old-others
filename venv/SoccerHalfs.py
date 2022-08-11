from playwright.sync_api import sync_playwright
from collections import Counter
from functools import reduce
import time
start = time.time()
url = "https://www.soccer24.com/match/rLor0PlM/#/match-summary"
def forming(page,link):                                    # NEED ADD TYPE SPORT AND FIXABLE CSS SELECTOR
    page.goto(link)
    matches = page.query_selector_all("[id^='g_1']")
    match_list = list()
    print(matches)
    for i in matches:
        line = i.inner_text()
        if "Awrd" in line:
            continue
        if "(0)" in line or "(1)" in line or "(2)" in line:
            match_list.append(line.split())

    return match_list
def first_half_results(matches,loc):
    team_scored = list()
    team_coceded = list()
    total_half = list()
    if loc == "home":
        scored,conceded = 2,3
    else:
        scored,conceded = 3,2
    for i in matches:
        scores = [j for j in i if j.isdigit() or j.isalnum() == False][-4:]
        if "(" in scores[0]:
            scores[0], scores[1], scores[2], scores[3] = scores[2], scores[3], scores[0], scores[1]
        team_scored.append(int(scores[scored].replace("(", "").replace(")", "")))
        team_coceded.append(int(scores[conceded].replace("(", "").replace(")", "")))
    return team_scored,team_coceded                # 0 -scored 1 - conceded
def separation_home_away(team_,all_matches):
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
            elif (i[1] == "AET" or i[2] == "AET" or i[1] == "Pen" or i[2] == "Pen") and i[3] in team_ and i[4] in team_:
                home_matches.append(i)
            else:
                away_matches.append(i)
    return home_matches,away_matches,count
def team_name(list):
    if len(list) > 0:
        team = set(reduce(lambda i, j: i & j, (set(x) for x in list)))
    else:
        team = ""
    return team
def summery(scores):
    return [i for i in scores]
def indication(list):
    null,one,more,amount = 0,0,0,0
    for i in list:
        amount += 1
        if i == 0:
            null += 1
        if i == 1:
            one += 1
        if i > 1:
            more += 1
    return null,one,more,amount

def teams_stat(link):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        chain = url.split("/")[1:3]
        team_home= 'https://'.join(chain)+page.query_selector_all('a.participant__participantName')[0].get_attribute(
            "href")
        team_away = 'https://'.join(chain)+page.query_selector_all('a.participant__participantName')[1].get_attribute(
            "href")
        link_hometeam_results = f'{team_home}/results/'
        link_awayteam_resalts =f'{team_away}/results/'
        home_name = team_name(forming(page,link_hometeam_results))
        away_name = team_name(forming(page,link_awayteam_resalts))
        home_results = separation_home_away(home_name,forming(page,link_hometeam_results))     # 0 - home, 1 - away
        away_results = separation_home_away(away_name,forming(page,link_awayteam_resalts))
        print(home_name,away_name)
        home_team_scores_list_at_home = summery(first_half_results(home_results[0],  loc="home")[0])
        home_team_conceded_list_at_home = summery(first_half_results(home_results[0],loc="home")[1])
        home_team_scores_list_away = summery(first_half_results(home_results[1],     loc="away")[0])
        home_team_conceded_list_away = summery(first_half_results(home_results[1],   loc="away")[1])
        away_team_scores_list_at_home = summery(first_half_results(away_results[0],  loc="home")[0])
        away_team_conceded_list_at_home = summery(first_half_results(away_results[0], loc="home")[1])
        away_team_scores_list_away = summery(first_half_results(away_results[1],     loc="away")[0])
        away_team_conceded_list_away = summery(first_half_results(away_results[1],    loc="away")[1])

        print(f"{home_name}  scored at home (0-1-more-all): ",indication(home_team_scores_list_at_home))
        print(home_team_scores_list_at_home)
        print(f"{home_name}  conceded at home (0-1-more-all): ",indication(home_team_conceded_list_at_home))
        print(home_team_conceded_list_at_home)
        print(f"{home_name}  scored as visitors (0-1-more-all): ",indication(home_team_scores_list_away))
        print(home_team_scores_list_away)
        print(f"{home_name}  conceded as visitors (0-1-more-all): ",indication(home_team_conceded_list_away))
        print(home_team_conceded_list_away)
        print("_________________AWAY__________________")
        print(f"{away_name}  scored at home (0-1-more-all): ",indication(away_team_scores_list_at_home ))
        print(away_team_scores_list_at_home )
        print(f"{away_name}  conceded at home (0-1-more-all): ",indication(away_team_conceded_list_at_home))
        print(away_team_conceded_list_at_home)
        print(f"{away_name}  scored as visitors (0-1-more-all): ",indication(away_team_scores_list_away))
        print(away_team_scores_list_away)
        print(f"{away_name}  conceded as visitors (0-1-more-all): ",indication(away_team_conceded_list_away))
        print(away_team_conceded_list_away)
teams_stat(url)
print(time.time() - start)

