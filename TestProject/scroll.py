from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
s = Service(r"C:\Users\anujp\PycharmProjects\TestProject\Browsers\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://leetcode.com")
time.sleep(3)
driver.execute_script("window.scrollBy(0,500)","")
time.sleep(3)
