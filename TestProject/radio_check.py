from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
s = Service(r"C:\Users\anujp\PycharmProjects\TestProject\Browsers\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://www.w3schools.com/html/html_forms.asp")
time.sleep(5)
driver.find_element(By.ID, "html").click()
time.sleep(2)
driver.find_element(By.ID,"vehicle1").click()
time.sleep(2)
driver.find_element(By.ID, "vehicle2").click()
time.sleep(2)
