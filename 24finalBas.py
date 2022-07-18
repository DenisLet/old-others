import requests
from bs4 import BeautifulSoup

url = "https://24score.pro/basketball/"
year = input("Enter year: ")
def get_matches(url):
    page = "https://24score.pro{}"
    soup = BeautifulSoup(requests.get(url).text,'html.parser')
    links = soup.select("#data_container td.team a")
    h2h = dict(zip([page.format(links[i].get("href")+year) for i in range(0,len(links),2)],
                   [page.format(links[i+1].get("href")+year) for i in range(0,len(links),2)]))
    return h2h

totals = int(input("Enter individual total: "))
totalsAll = int(input("Total: "))
def get_scores(get_matches,totals,totalsAll):
    response = requests.get(get_matches)
    soup = BeautifulSoup(response.text, 'lxml')
    scores_home = soup.select("#data_container div.data10_home td.score")
    scores_away = soup.select("#data_container div.data10_away td.score")
    allwin, allwin3 = 0, 0
    alllose, alllose3 = 0, 0
    more = 0
    allow_to_score = 0
    moreAll = 0
    lessAll = 0
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
        if home1 > totals or home2 > totals or home3 > totals or home4 > totals:
            print("M---O---R---E   I---N---D")
            more += 1
        if away1 > totals or away2 > totals or away3 > totals or away4 > totals:
            allow_to_score += 1
            print("A---L---L---O---W   I---N---D")
        if home1 + away1 > totalsAll or home2 + away2 > totalsAll or home3 + away3 > totalsAll or home4 + away4 > totalsAll:
            print("M---O---R---E")
            moreAll += 1
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
        if away1 > totals or away2 > totals or away3 > totals or away4 > totals:
            more += 1
            print("M---O---R---E   I---N---D")
        if home1 > totals or home2 > totals or home3 > totals or home4 > totals:
            allow_to_score += 1
            print("A---L---L---O---W   I---N---D")
        if home1 + away1 > totalsAll or home2 + away2 > totalsAll or home3 + away3 > totalsAll or home4 + away4 > totalsAll:
            print("M---O---R---E")
            moreAll += 1
        count += 1
    print("For 4 Qwtrs: ", count, "WIN:", allwin, "LOSS:", alllose)
    print("For 3 Qwtrs: ", count, "WIN:", allwin3, "LOSS:", alllose3)
    print(count, "More Then (individual){}:".format(totals), more, "Allow: ", allow_to_score)
    print(count, "More Then both({}):".format(totalsAll), moreAll)

for i,j in get_matches(url).items():
    print(i.split("/")[6]+j.split("/")[6])
    get_scores(i,totals,totalsAll)
    print()
    get_scores(j,totals,totalsAll)
    print("NEXT MATCH")









