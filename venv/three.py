from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/wait1.html")

button = browser.find_element(By.ID, "verify")
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text

# lis = ['15.12.2021', 'AET', 'Hannover-Burgdorf', 'Kiel', '28', '30', '13', '12', '12', '13', '3', '5', 'W']
# lis1 =['29.04.', '21:00', 'Zaglebie', 'Vive', 'Kielce', '24', '32', '11', '15', '13', '17', 'L']
# lis2 = ['23.11.2021', 'Pen', 'Zaglebie', 'Chrobry', 'Glogow', '33', '35', '17', '16', '14', '15', '2', '4', 'L']
# # print(lis[-9:])
# # print(lis1[-9:])
# # print(lis2[-9:])
# print([i for i in lis1 if i.isdigit()][2:6])
