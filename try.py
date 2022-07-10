import re
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


rs = requests.get('https://www.handball24.com/match/tt9ewWsa/#/match-summary')
root = BeautifulSoup(rs.content, 'html.parser')

for x in root.select('#detail'):
    m = re.search(r"url\((.+?)\)", x["href"])
    print(m)