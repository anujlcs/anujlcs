from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

service=Service(r"C:\Users\anujp\PycharmProjects\TestProject_2\Browser\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://www.facebook.com/")
driver.find_element(By.PARTIAL_LINK_TEXT, "Create New Account").click()
time.sleep(3)
driver.find_element(By.NAME, "firstname").send_keys("Anuj")
time.sleep(2)
driver.find_element(By.NAME, "lastname").send_keys("Pandey")
time.sleep(2)
driver.find_element(By.NAME, "reg_email__").send_keys("8896519885")
time.sleep(2)
driver.find_element(By.ID, "password_step_input").send_keys("8896519885")
time.sleep(2)
sel = Select(driver.find_element(By.ID, "day"))
sel.select_by_visible_text("10")
sel_2 = Select(driver.find_element(By.ID, "month"))
sel_2.select_by_visible_text("Jun")
sel_3 = Select(driver.find_element(By.ID, "year"))
sel_3.select_by_visible_text("2021")
driver.find_element(By.XPATH, "//*[@id='u_2_o_5r']/span[2]/label").click()
