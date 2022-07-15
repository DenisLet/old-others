import requests
from bs4 import BeautifulSoup
url = "https://24score.pro/basketball/"
def get_matches(url):
    page = "https://24score.pro"
    soup = BeautifulSoup(requests.get(url).text,'html.parser')
    links = soup.select("#data_container td.team a")
    h2h = dict(zip(["{}{}".format(page,links[i].get("href")) for i in range(0,len(links),2)],
                   ["{}{}".format(page,links[i+1].get("href")) for i in range(0,len(links),2)]))
    return h2h
print(get_matches(url))