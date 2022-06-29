import requests
from bs4 import BeautifulSoup
url_home = input("HOME:")
# url_away = input("AWAY:")
def home(url_home):
    url = url_home
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    scores = soup.select("#data_container div.data10_home td.score")
    clearance(scores)

def away(url_home):
    url = url_home
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    scores = soup.select("#data_container div.data10_away td.score")
    clearance(scores)



def clearance(scores):
    total_1st, total_2nd, total_3rd, total_4th = [], [], [], []
    homeScore1, homeScore2, homeScore3, homeScore4 = [], [], [], []
    awayScore1, awayScore2, awayScore3, awayScore4 = [], [], [], []
    totalHome, totalAway = [], []
    for score in scores:
        if "— —" in score.text or "Отложен" in score.text:
            continue
        xline=score.findAll(text=True,recursive=False).pop(1).replace("OT","")\
            .replace("(","").replace(")","").replace(" ","").strip().split(",")
        review(xline,total_1st,total_2nd,total_3rd,total_4th,homeScore1, homeScore2, homeScore3, homeScore4,\
           awayScore1, awayScore2, awayScore3, awayScore4,totalHome, totalAway)
    total_1st.sort(), total_2nd.sort(), total_3rd.sort(), total_4th.sort()
    homeScore1.sort(), homeScore2.sort(), homeScore3.sort(), homeScore4.sort()
    awayScore1.sort(), awayScore2.sort(), awayScore3.sort(), awayScore4.sort()
    totalHome.sort()
    totalAway.sort()


def review(xline,total_1st,total_2nd,total_3rd,total_4th,homeScore1, homeScore2, homeScore3, homeScore4,\
           awayScore1, awayScore2, awayScore3, awayScore4,totalHome, totalAway):
    firstQ,secondQ,thirdQ,fourthQ=xline[0],xline[1],xline[2],xline[3]
    home1, away1 = int(firstQ.split(":")[0]), int(firstQ.split(":")[1])
    home2, away2 = int(secondQ.split(":")[0]), int(secondQ.split(":")[1])
    home3, away3 = int(thirdQ.split(":")[0]), int(thirdQ.split(":")[1])
    home4, away4 = int(fourthQ.split(":")[0]), int(fourthQ.split(":")[1])
    total_1st.append(home1+away1),total_2nd.append(home2+away2)
    total_3rd.append(home3+away3),total_4th.append(home4+away4)
    homeScore1.append(home1),homeScore2.append(home2),homeScore3.append(home3),homeScore4.append(home4)
    awayScore1.append(away1),awayScore2.append(away2),awayScore3.append(away3),awayScore4.append(away4)
    totalHome.append(home1+home2+home3+home4),totalAway.append(away1+away2+away3+away4)
    print(xline,home1+away1,home2+away2,home3+away3,home4+away4)
    print(home1+home2+home3+home4,":",away1+away2+away3+away4)

home(url_home)
print()
away(url_home)

