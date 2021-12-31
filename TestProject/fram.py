from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
s=Service(r"C:\Users\anujp\PycharmProjects\TestProject\Browsers\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
driver.switch_to.frame("packageListFrame")
time.sleep(3)
driver.find_element(By.LINK_TEXT,"org.openqa.selenium").click()
driver.switch_to.default_content()
time.sleep(3)
driver.switch_to.frame("packageFrame")
driver.find_element(By.LINK_TEXT,"Alert").click()
driver.switch_to.default_content() #we right this command when switch from one frame to another frame
time.sleep(3)
driver.switch_to.frame("classFrame")
driver.find_element(By.XPATH, '//*[@id="i0"]/th/code/span/a').click()
