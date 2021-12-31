from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
s = Service(r"C:\Users\anujp\PycharmProjects\TestProject\Browsers\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("http://testautomationpractice.blogspot.com/")
driver.execute_script("window.scrollBy(0,100)","")
time.sleep(3)
action = ActionChains(driver)
source = driver.find_element(By.ID, "draggable")
time.sleep(3)
target = driver.find_element(By.ID, "droppable")
action.drag_and_drop(source,target).perform()
time.sleep(3)
