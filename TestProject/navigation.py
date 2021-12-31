from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
s = Service(r"C:\Users\anujp\PycharmProjects\TestProject\Browsers\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://google.com")
time.sleep(2)
driver.find_element(By.NAME, "q"). send_keys("facebook.com")
time.sleep(1)
driver.find_element(By.NAME, "btnK").send_keys(Keys.ENTER)
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
driver.refresh()
driver.close()
#driver.close()
