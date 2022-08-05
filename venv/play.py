from playwright.sync_api import sync_playwright
from collections import Counter
url = "https://www.soccer24.com/match/Q5x2SpTj/#/match-summary/match-summary"
def teams(link):
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
        page.goto(link_hometeam_results)
        matches = page.query_selector_all("[id^='g_1']")
        match_list, home_matches, away_matches = [], [], []
        first_half_home,fulltime_home = [],[]
        first_half_away,fulltime_away = [],[]
        for i in matches:
            # print(i.inner_text().split())
            match_list.append(i.inner_text().split())
        team_set = set(match_list[0]) & set(match_list[1]) & set(match_list[2])\
                   & set(match_list[3]) & set(match_list[4])& set(match_list[5])\
                   & set(match_list[6]) & set(match_list[7])& set(match_list[8])\
                   & set(match_list[9]) & set(match_list[10]) & set(match_list[11])\
                   & set(match_list[12]) & set(match_list[13])& set(match_list[14])\
                   & set(match_list[15]) & set(match_list[16])& set(match_list[17])

        print(team_set)
        count = 0
        for i in match_list:
            count += 1
            if len(team_set) == 1:
                if i[1] in team_set:
                    home_matches.append(i)
                elif i[2] in team_set and ":" in i[1] :
                    home_matches.append(i)
                elif (i[1] == "AET" or i[2] == "AET") and i[3] in team_set:
                    home_matches.append(i)
                else:
                    away_matches.append(i)
            else:
                if i[1] in team_set and i[2] in team_set:
                    home_matches.append(i)
                elif i[2] in team_set and i[3] in team_set and ":" in i[1] :
                    home_matches.append(i)
                elif (i[1] == "AET" or i[2] == "AET") and i[3] in team_set and i[4] in team_set:
                    home_matches.append(i)
                else:
                    away_matches.append(i)

        for i in home_matches:
            print(i,"HOME")
        for i in away_matches:
            print(i,"AWAY")

        for i in home_matches:
            scores = [j for j in i if j.isdigit() or j.isalnum() == False][-4:]
            if "(" in scores[0]:
                scores[0],scores[1],scores[2],scores[3] = scores[2],scores[3],scores[0],scores[1]
            first_half_home.append(int(scores[2].replace("(","").replace(")",""))+int(scores[3].replace(
                "(","").replace(")","")))
            fulltime_home.append(int(scores[0])+int(scores[1]))
            print(scores)
        print("________________________________________________________________________________________")
        for i in away_matches:
            scores = [j for j in i if j.isdigit() or j.isalnum() == False][-4:]
            if "(" in scores[0]:
                scores[0],scores[1],scores[2],scores[3] = scores[2],scores[3],scores[0],scores[1]
            print(scores)
            first_half_away.append(int(scores[2].replace("(", "").replace(")", "")) + int(scores[3].replace(
                "(", "").replace(")", "")))
            fulltime_away.append(int(scores[0]) + int(scores[1]))
        null,one,more = 0,0,0
        for i in first_half_home:
            if i == 0:
                null += 1
            elif i == 1:
                one += 1
            else:
                more += 1

        print(null,one,more)
        # for i,k in Counter(first_half_home).items():
        #     if i == 0:
        #         print(i,f'{k}/{len(first_half_home)}')
        #     elif i == 1:
        #         print(i, f'{k}/{len(first_half_home)}')
        # for i,k in Counter(first_half_away).items():
        #     if i == 0:
        #         print(i,f'{k}/{len(first_half_away)}')
        #     elif i == 1:
        #         print(i, f'{k}/{len(first_half_away)}')



        # print(Counter(first_half_home),len(first_half_home))
        # print(Counter(fulltime_home))
        # print(Counter(first_half_away),len(first_half_away))
        # print(Counter(fulltime_away))
        return count


teams(url)


