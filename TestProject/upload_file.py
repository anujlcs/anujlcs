from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
s = Service(r"C:\Users\anujp\PycharmProjects\TestProject\Browsers\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("http://testautomationpractice.blogspot.com/")
driver.execute_script("window.scrollBy(0,1000)","")
driver.switch_to.frame("frame-one1434677811")
file = driver.find_element(By.NAME, "RESULT_FileUpload-10")
file.send_keys("C:\\Users\\anujp\\\Desktop\\pexels-pixabay-45246.jpg")
time.sleep(5)
