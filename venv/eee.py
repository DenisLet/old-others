from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from functools import reduce
import time

url = "https://www.icehockey24.com/team/sibir-novosibirsk/QoNOI7Jo/results/"
browser = webdriver.Chrome()
browser.get(url)

team = browser.find_element(By.CLASS_NAME,"heading__name").get_attribute("innerHTML")
print(team)
time.sleep(4)
browser.quit()