from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
s=Service(r"C:\Users\anujp\PycharmProjects\TestProject_2\Browser\chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("https://www.google.com")
driver.maximize_window()
text=driver.find_element(By.NAME, "q")
text.click()
time.sleep(2)
text.send_keys("goibibo")
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]").send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT, "GoIbibo™ Official Website - Flat 10% Off, Code: SAVEMORE").click()
time.sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT, "Hotels").click()
time.sleep(2)
driver.find_element(By.NAME, "CountryType").click()
time.sleep(2)
search = driver.find_element(By.XPATH, "//*[@id='downshift-1-input']")
search.click()
time.sleep(2)
search.send_keys("Lucknow")
time.sleep(2)
search.send_keys(Keys.ARROW_DOWN)

driver.find_element(By.XPATH, "//*[@id='downshift-1-menu']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div/section[1]/div[1]/div/div[3]/div/div[1]").click()
time.sleep(2)
month = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div/section[1]/div[1]/div[2]/div[3]/div/div[1]/div[2]/section/div/div[2]/div[1]/span[1]")
arrow=driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div/section[1]/div[1]/div[2]/div[3]/div/div[1]/div[2]/section/div/div[2]/div[1]/span[2]")
while (month.text != "May 2022"):
    arrow.click()
    time.sleep(1)
    if(month.text == "May 2022"):
        break
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div/section[1]/div[1]/div[2]/div[3]/div/div[1]/div[2]/section/div/div[1]/div[2]/div/ul[2]/li[18]/span").click()
time.sleep(3)
driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div/section[1]/div[1]/div[2]/div[3]/div/div[1]/div[2]/section/div/div[1]/div[2]/div/ul[2]/li[26]/span").click()
time.sleep(10)

driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div/section[1]/div[1]/div/button").send_keys(Keys.ENTER)
time.sleep(2)

