from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
s = Service(r"C:\Users\anujp\PycharmProjects\TestProject\Browsers\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://demoqa.com/select-menu")

# select by visiblw_text
var = Select(driver.find_element(By.ID, "oldSelectMenu"))
var.select_by_visible_text("Green")

# select by value

#select by index








"""driver.get("https://www.selenium.dev/documentation/webdriver/waits/")
driver.find_element(By.ID, "navbarDropdown").click()
time.sleep(5)
driver.find_element(By.CLASS_NAME, "dropdown-item").click()"""
