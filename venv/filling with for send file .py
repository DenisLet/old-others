import os.path
import typing
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
try:
    www = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(www)
    for inp in browser.find_elements_by_css_selector(".form-group input"):
        inp.send_keys("data")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = os.path.join(current_dir,'testtext.txt')
    print(file_name)
    browser.find_element(By.CSS_SELECTOR,"[type='file']").send_keys(file_name)
    browser.find_element(By.CSS_SELECTOR,"[type='submit']").click()
    alert = browser.switch_to.alert
    print(alert.text)
finally:
    time.sleep(7)
    browser.quit()