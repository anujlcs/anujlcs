from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
s = Service(r"C:\Users\anujp\PycharmProjects\TestProject_2\Browser\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://youtube.com")
time.sleep(2)

# sign in
sign = driver.find_element(By.XPATH, "//*[@id='buttons']/ytd-button-renderer")
sign.click()
# email
time.sleep(2)
email = driver.find_element(By.NAME, "identifier")
email.click()
email.send_keys("Enter your mail")
time.sleep(2)
# button
button = driver.find_element(By.XPATH, "//*[@id='identifierNext']/div/button")
button.click()
time.sleep(2)
# password
password = driver.find_element(By.NAME, "password")
password.click()
password.send_keys("Enter your password")
# button_2
next = driver.find_element(By.XPATH, "//*[@id='passwordNext']/div/button")
next.click()
