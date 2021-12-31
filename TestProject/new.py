from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
s=Service(r"C:\Users\anujp\PycharmProjects\TestProject\Browsers\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("http://testautomationpractice.blogspot.com/")
driver.find_element(By.XPATH, "//*[@id='HTML9']/div[1]/button").click()
driver.swi1tch_to_alert

