from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
s = Service(r"C:\Users\anujp\PycharmProjects\TestProject\Browsers\chromedriver.exe")
driver = webdriver.Chrome(service=s)
#driver.get("https://leetcode.com/accounts/login/")
driver.get("https://tutorialdeep.com/knowhow/show-different-form-radio-button-selection/")
time.sleep(2)
"""var = driver.find_element(By.NAME, "login")
print(var.is_displayed())
print(var.is_enabled())"""
var2 = driver.find_element(By.NAME, "demo")
print(var2.is_selected())

