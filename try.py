import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
link = "https://www.handball24.com/team/iceland/OdLMxcTM{}".format("/results/")
browser = webdriver.Chrome()
browser.get(link)
link = "https://www.handball24.com/team/bergischer/UJnQvkWb/"
browser.get(link)