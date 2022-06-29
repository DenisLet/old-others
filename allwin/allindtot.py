import requests
from bs4 import BeautifulSoup
year = 2021
url = "https://24score.pro/basketball/team/new_zealand/taranaki_mountainairs_(m)/{}".format(year)
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
scores=soup.select("#data_container div.data10_home td.score")
total_1st,total_2nd,total_3rd,total_4th=[],[],[],[]
homeScore1,homeScore2,homeScore3,homeScore4=[],[],[],[]
awayScore1,awayScore2,awayScore3,awayScore4=[],[],[],[]
totalHome,totalAway=[],[]
totals = int(input("Total: "))
totalmatch=[]
count=0
more = 0
allow_to_score=0
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
    total_1st.append(home1+away1),total_2nd.append(home2+away2)
    total_3rd.append(home3+away3),total_4th.append(home4+away4)
    homeScore1.append(home1),homeScore2.append(home2),homeScore3.append(home3),homeScore4.append(home4)
    awayScore1.append(away1),awayScore2.append(away2),awayScore3.append(away3),awayScore4.append(away4)
    totalHome.append(home1+home2+home3+home4),totalAway.append(away1+away2+away3+away4),totalmatch.append( \
        home1 + home2 + home3 + home4 + away1+away2+away3+away4 )
    print(xline)
    if home1 > totals or home2 > totals or home3 > totals or home4 > totals:
        print("M---O---R---E")
        more+=1
    if away1 > totals or away2 > totals or away3 > totals or away4 > totals:
        allow_to_score+=1
        print("A---L---L---O---W")



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
    total_1st.append(home1+away1),total_2nd.append(home2+away2)
    total_3rd.append(home3+away3),total_4th.append(home4+away4)
    homeScore1.append(home1),homeScore2.append(home2),homeScore3.append(home3),homeScore4.append(home4)
    awayScore1.append(away1),awayScore2.append(away2),awayScore3.append(away3),awayScore4.append(away4)
    totalHome.append(home1+home2+home3+home4),totalAway.append(away1+away2+away3+away4),totalmatch.append( \
        home1 + home2 + home3 + home4 + away1+away2+away3+away4 )
    print(xline)
    if away1 > totals or away2 > totals or away3 > totals or away4 > totals:
        more+=1
        print("M---O---R---E")
    if home1 > totals or home2 > totals or home3 > totals or home4 > totals:
        allow_to_score+=1
        print("A---L---L---O---W")
    count += 1






















total_1st.sort(),total_2nd.sort(),total_3rd.sort(),total_4th.sort()
homeScore1.sort(),homeScore2.sort(),homeScore3.sort(),homeScore4.sort()
awayScore1.sort(),awayScore2.sort(),awayScore3.sort(),awayScore4.sort()
totalHome.sort()
totalAway.sort(),totalmatch.sort()
print(count,"More Then",more,"Allow: ",allow_to_score  )
































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
