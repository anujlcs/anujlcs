"""from selenium import webdriver
import time
from selenium .webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
s = Service(r"C:\Users\anujp\PycharmProjects\TestProject\Browsers\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://www.javatpoint.com/contact-us")
time.sleep(2)

name = driver.find_element(By.NAME, "name")
name.send_keys("Anuj Pandey")
time.sleep(2)

mobile = driver.find_element(By.NAME, "mobile")
mobile.send_keys("8115563192")
time.sleep(2)

email = driver.find_element(By.NAME, "email")
email.send_keys("anujpandey0507@gmail.com")
time.sleep(2)

course = driver.find_element(By.NAME, "course")
course.send_keys("Python")
time.sleep(2)

message = driver.find_element(By.NAME, "message")
message.send_keys("May be i am write a correct script")
time.sleep(2)

button = driver.find_element(By.CLASS_NAME, "subbutton")
button.click()"""



