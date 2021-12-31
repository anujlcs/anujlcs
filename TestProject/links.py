from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
s = Service(r"C:\Users\anujp\PycharmProjects\TestProject\Browsers\chromedriver.exe")
driver = webdriver.Chrome(service = s)
driver.get("https://www.google.com/search?client=firefox-b-d&q=w3schools")
#var = driver.find_elements(By.TAG_NAME,"a")
#print(len(var))  # for number of links available in page

links = driver.find_elements(By.TAG_NAME, "a") # for printing the text of links in a web page.
for i in links:
    print(i.text)
