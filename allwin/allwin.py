import requests
from bs4 import BeautifulSoup
year = 2022
url = "https://24score.pro/basketball/team/new_zealand/franklin_bulls_(m)/{}".format(year)
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
scores=soup.select("#data_container div.data10_home td.score")
count=0
allwin,allwin3 = 0,0
alllose,alllose3 = 0,0
for score in scores:
    if "— —" in score.text or "Отложен" in score.text or "тех. пор." in score.text:
        continue
    xline=score.findAll(text=True,recursive=False).pop(1).replace("OT","")\
        .replace("(","").replace(")","").replace(" ","").strip().split(",")

    firstQ,secondQ,thirdQ,fourthQ=xline[0],xline[1],xline[2],xline[3]
    home1, away1 = int(firstQ.split(":")[0]), int(firstQ.split(":")[1])
    home2, away2 = int(secondQ.split(":")[0]), int(secondQ.split(":")[1])
    home3, away3 = int(thirdQ.split(":")[0]), int(thirdQ.split(":")[1])
    home4, away4 = int(fourthQ.split(":")[0]), int(fourthQ.split(":")[1])
    print(xline)
    # print(home1+home2+home3+home4,":",away1+away2+away3+away4)

    if home1 >= away1 and home2 >= away2 and home3 >= away3:
        allwin3+=1
        print("W----I----N   A----L----L----3")
        if home4 >=away4:
            print("W----I----N   A----L----L")
            allwin+=1

    if home1 <= away1 and home2 <= away2 and home3 <= away3:

        alllose3+=1
        print("L----O----S----E   A----L----L----3")
        if home4 <= away4:
            alllose+=1
            print("L----O----S----E   A----L----L")
    count += 1
print()
print("_______________AWAY__________________")
print()
scores = scores=soup.select("#data_container div.data10_away td.score")

for score in scores:
    if "— —" in score.text or "Отложен" in score.text or "тех. пор." in score.text:
        continue
    xline=score.findAll(text=True,recursive=False).pop(1).replace("OT","")\
        .replace("(","").replace(")","").replace(" ","").strip().split(",")
    firstQ,secondQ,thirdQ,fourthQ=xline[0],xline[1],xline[2],xline[3]
    home1, away1 = int(firstQ.split(":")[0]), int(firstQ.split(":")[1])
    home2, away2 = int(secondQ.split(":")[0]), int(secondQ.split(":")[1])
    home3, away3 = int(thirdQ.split(":")[0]), int(thirdQ.split(":")[1])
    home4, away4 = int(fourthQ.split(":")[0]), int(fourthQ.split(":")[1])
    print(xline)
    if home1 <= away1 and home2 <= away2 and home3 <= away3:
        allwin3+=1
        print("W----I----N   A----L----L----3")
        if home4 <= away4:
            allwin+=1
            print("W----I----N   A----L----L")
    if home1 >= away1 and home2 >= away2 and home3 >= away3 and home4 >= away4:
        alllose3+=1
        print("L----O----S----E   A----L----L----3")
        if home4 >= away4:
            alllose+=1
            print("L----O----S----E   A----L----L")
    count += 1
print("For 4 Qwtrs: ",count,"WIN:",allwin,"LOSS:",alllose)
print("For 3 Qwtrs: ",count,"WIN:",allwin3,"LOSS:",alllose3)
































# print("1ST QTR:",total_1st)
# print("1ST IND:",homeScore1)
# print()
# print("2ND QTR:",total_2nd)
# print("2ND IND:",homeScore2)
# print()
# print("3RD QTR:",total_3rd)
# print("3RD IND:",homeScore3)
# print()
# print("4TH QTR:",total_4th)
# print("4TH IND:",homeScore4)
# print()
# print("TOTAL IND:",totalHome)
# print(totalmatch)
