import requests
from bs4 import BeautifulSoup
YAER = 2022
url = "https://24score.pro/basketball/"
def get_matches(url):
    page = "https://24score.pro{}"
    soup = BeautifulSoup(requests.get(url).text,'html.parser')
    links = soup.select("#data_container td.team a")
    h2h = dict(zip([page.format(links[i].get("href")) for i in range(0,len(links),2)],
                   [page.format(links[i+1].get("href")) for i in range(0,len(links),2)]))
    return h2h

def get_scores(get_matches):
    response = requests.get(get_matches)
    soup = BeautifulSoup(response.text, 'lxml')
    scores_home = soup.select("#data_container div.data10_home td.score")
    scores_away = soup.select("#data_container div.data10_away td.score")
    allwin, allwin3 = 0, 0
    alllose, alllose3 = 0, 0
    count = 0
    for score in scores_home:
        if "— —" in score.text or "Отложен" in score.text or "тех. пор." in score.text:
            continue
        xline = score.findAll(text=True, recursive=False).pop(1).replace("OT", "") \
            .replace("(", "").replace(")", "").replace(" ", "").strip().split(",")
        firstQ, secondQ, thirdQ, fourthQ = xline[0], xline[1], xline[2], xline[3]
        home1, away1 = int(firstQ.split(":")[0]), int(firstQ.split(":")[1])
        home2, away2 = int(secondQ.split(":")[0]), int(secondQ.split(":")[1])
        home3, away3 = int(thirdQ.split(":")[0]), int(thirdQ.split(":")[1])
        home4, away4 = int(fourthQ.split(":")[0]), int(fourthQ.split(":")[1])
        print(xline)
        if home1 >= away1 and home2 >= away2 and home3 >= away3:
            allwin3 += 1
            print("W----I----N   A----L----L----3")
            if home4 >= away4:
                print("W----I----N   A----L----L")
                allwin += 1
        if home1 <= away1 and home2 <= away2 and home3 <= away3:
            alllose3 += 1
            print("L----O----S----E   A----L----L----3")
            if home4 <= away4:
                alllose += 1
                print("L----O----S----E   A----L----L")
        count += 1
    for score in scores_away:
        if "— —" in score.text or "Отложен" in score.text or "тех. пор." in score.text:
            continue
        xline = score.findAll(text=True, recursive=False).pop(1).replace("OT", "") \
            .replace("(", "").replace(")", "").replace(" ", "").strip().split(",")
        firstQ, secondQ, thirdQ, fourthQ = xline[0], xline[1], xline[2], xline[3]
        home1, away1 = int(firstQ.split(":")[0]), int(firstQ.split(":")[1])
        home2, away2 = int(secondQ.split(":")[0]), int(secondQ.split(":")[1])
        home3, away3 = int(thirdQ.split(":")[0]), int(thirdQ.split(":")[1])
        home4, away4 = int(fourthQ.split(":")[0]), int(fourthQ.split(":")[1])
        print(xline)
        if home1 <= away1 and home2 <= away2 and home3 <= away3:
            allwin3 += 1
            print("W----I----N   A----L----L----3")
            if home4 <= away4:
                allwin += 1
                print("W----I----N   A----L----L")
        if home1 >= away1 and home2 >= away2 and home3 >= away3 and home4 >= away4:
            alllose3 += 1
            print("L----O----S----E   A----L----L----3")
            if home4 >= away4:
                alllose += 1
                print("L----O----S----E   A----L----L")
        count += 1
    print("For 4 Qwtrs: ", count, "WIN:", allwin, "LOSS:", alllose)
    print("For 3 Qwtrs: ", count, "WIN:", allwin3, "LOSS:", alllose3)

for i,j in get_matches(url).items():
    get_scores(i)
    print()
    get_scores(j)
    print("NEXT MATCH")









