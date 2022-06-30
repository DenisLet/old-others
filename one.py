import requests
from bs4 import BeautifulSoup
url = 'https://24score.pro/basketball/team/usa/ny_knicks_(m)/2019/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
scores=soup.select("#data_container div.data10_all td.score")
total_1st,total_2nd,total_3rd,total_4th=[],[],[],[]
for score in scores:
    if "— —" in score.text or "Отложен" in score.text:
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
    print(xline)
    print(home1+away1,home2+away2,home3+away3,home4+away4,sep="        ")
print(min(total_1st),max(total_1st))
print(min(total_2nd),max(total_2nd))
print(min(total_3rd),max(total_3rd))
print(min(total_4th),max(total_4th))