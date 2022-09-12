from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from functools import reduce
import time

url = "https://www.icehockey24.com/team/spartak-moscow/vkRSHRYi/results/"
caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "eager"
browser = webdriver.Chrome(desired_capabilities=caps)
browser.get(url)

browser.execute_script("arguments[0].click();", WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.event__more.event__more--static"))))

time.sleep(10)
browser.quit()