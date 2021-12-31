from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
service = Service(r"C:\Users\anujp\PycharmProjects\TestProject\Browsers\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://google.com")
print(driver.title)
time.sleep(1)
driver.find_element(By.NAME, "q").send_keys("leetcode login")
time.sleep(1)
driver.find_element(By.NAME, "btnK").send_keys(Keys.ENTER)
time.sleep(1)
driver.find_element(By.PARTIAL_LINK_TEXT, "Account Login - LeetCode").click()
time.sleep(1)
driver.find_element(By.CLASS_NAME, "input__2o8B ").send_keys("anujpandey0507@gmail.com")
time.sleep(1)
driver.find_element(By.NAME, "password").send_keys("kcnitbanda1999")
time.sleep(1)
driver.find_element(By.ID, "signin_btn").send_keys(Keys.ENTER)
"""driver.find_element(By.NAME, "").send_keys("")
time.sleep(1)
driver.find_element(By.CLASS_NAME, "").send_keys(Keys.ENTER)
#driver.close()"""