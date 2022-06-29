import requests
from bs4 import BeautifulSoup
import re

url = 'https://24score.pro/ice_hockey/team/usa/tucson/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
scores = soup.select("#data_container div.data10_home td.score")
for score in scores:
    if "— —" in score.text or "Отложен" in score.text:
        continue
    xline = score.findAll(text=True, recursive=False).pop(1).replace("OT", "") \
        .replace("(", "").replace(")", "").replace(" ", "").strip().split(",")
    firstQ, secondQ, thirdQ, fourthQ = xline[0], xline[1], xline[2], xline[3]
    print(firstQ.split(":")[0], firstQ.split(":")[1])
