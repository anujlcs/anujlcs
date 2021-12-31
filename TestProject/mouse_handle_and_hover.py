from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
s=Service(r"C:\Users\anujp\PycharmProjects\TestProject\Browsers\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://edureka.co")
time.sleep(3)
action = ActionChains(driver)
nav = driver.find_element(By.XPATH, "/html/body/nav/div[1]/a/span")
action.move_to_element(nav).perform()
time.sleep(3)
subnav = driver.find_element(By.XPATH, "/html/body/nav/div[1]/ul/li[1]/a")
subnav.click()
#subnav2 = driver.find_element(By.XPATH,"/html/body/nav/div[1]/ul/li[1]/ul/li[1]/a")
#subnav2.click()



#/html/body/nav