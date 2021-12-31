from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
s = Service(r"C:\Users\anujp\PycharmProjects\TestProject\Browsers\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://selenium-python.readthedocs.io/")
cook = driver.get_cookies()
for i in cook:
    print(i)

time.sleep(2)
