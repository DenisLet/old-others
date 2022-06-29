
url_home = input("HOME:")
url_away = input("AWAY:")
while True:
    import requests
    from bs4 import BeautifulSoup
    import itertools
    # url_home = input("HOME:")
    # url_away = input("AWAY:")
    score_input = input("Enter score of 1st period: ")
    def home(url_home,score_input):
        url=url_home
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        scores_home = soup.select("#data_container div.data10_home td.score")
        k = 0
        k1 = 0
        k2 = 0
        score00_home = 0
        score_0110_home = 0
        score2_home = 0
        score_2andmore_home = 0
        score00_away = 0
        score_0110_away = 0
        score2_away = 0
        score_2andmore_away = 0
        home = []
        away = []
        for score in scores_home:
            xline = score.text.strip() \
                .replace("В", "") \
                .replace("П", "") \
                .replace("OT", "") \
                .replace("пен", "").replace(")", "").replace("\t", "").replace("\n", "")
            if "— —" == xline:
                continue
            xline2 = xline.replace("(", ",")

            if score_input in xline2[4:7]:  # main condition
                k += 1
                k1 += 1
                print(xline2[4:7])
                summ = int(xline2[11]) + int(xline2[9])
                if summ > 2:
                    score_2andmore_home += 1
                    score2_home += 0
                    score_0110_home += 0
                    score00_home += 0
                elif summ == 2:
                    score_2andmore_home += 0
                    score2_home += 1
                    score_0110_home += 0
                    score00_home += 0
                elif summ == 1:
                    score_2andmore_home += 0
                    score2_home += 0
                    score_0110_home += 1
                    score00_home += 0
                elif summ == 0:
                    score_2andmore_home += 0
                    score2_home += 0
                    score_0110_home += 0
                    score00_home += 1
                home.append(xline2[9:12])
        print("HOME: ", home, k1, "cases")
        print("0 GOAL:", score00_home, "     1 GAOL:", score_0110_home, "     2 GAOLS:", score2_home, "     2+GOALS:",
              score_2andmore_home)
        print("HOME STATS GOAL PROBABILITY:", f"{(k1 - score00_home) / k1:.0%}")
    def away(url_away,score_input):
        url=url_away
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        scores_away = soup.select("#data_container div.data10_away td.score")
        k = 0
        k1 = 0
        k2 = 0
        score00_home = 0
        score_0110_home = 0
        score2_home = 0
        score_2andmore_home = 0
        score00_away = 0
        score_0110_away = 0
        score2_away = 0
        score_2andmore_away = 0
        home = []
        away = []
        for score in scores_away:
            xline = score.text.strip() \
                .replace("В", "") \
                .replace("П", "") \
                .replace("OT", "") \
                .replace("пен", "").replace(")", "").replace("\t", "").replace("\n", "")
            if "— —" == xline:
                continue
            xline2 = xline.replace("(", ",")
            if score_input in xline2[4:7]:  # main condition
                k += 1
                k2 += 1
                print(xline2[4:7])
                summ = int(xline2[11]) + int(xline2[9])
                if summ > 2:
                    score_2andmore_away += 1
                    score2_away += 0
                    score_0110_away += 0
                    score00_away += 0
                elif summ == 2:
                    score_2andmore_away += 0
                    score2_away += 1
                    score_0110_away += 0
                    score00_away += 0
                elif summ == 1:
                    score_2andmore_away += 0
                    score2_away += 0
                    score_0110_away += 1
                    score00_away += 0
                elif summ == 0:
                    score_2andmore_away += 0
                    score2_away += 0
                    score_0110_away += 0
                    score00_away += 1
                away.append(xline2[9:12])
        # print("TOTAL STATS GOAL PROBABILITY:", f"{(k - score00_home - score00_away) / k:.0%}", "     TOTAL CASES:", k)
        print("AWAY: ", away, k2, "cases")
        print("0 GOAL:", score00_away, "     1 GAOL:", score_0110_away, "     2 GAOLS:", score2_away, "     2+GOALS:",
              score_2andmore_away)
        print("AWAY STATS GOAL PROBABILITY:", f"{(k2 - score00_away) / k2:.0%}")
    home(url_home,score_input)
    away(url_away,score_input)
