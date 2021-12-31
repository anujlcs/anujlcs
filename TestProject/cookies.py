from selenium import webdriver
from selenium.webdriver.chrome.service import Service
s = Service(r"C:\Users\anujp\PycharmProjects\TestProject\Browsers\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.selenium.dev/documentation/webdriver/")
# Adds the cookie into current browser context
driver.add_cookie({"name": "anuj", "value": "venv"})
driver.add_cookie({"name": "key", "value": "value"})
#print(driver.get_cookies())
#print(driver.get_cookie("key"))
#driver.delete_cookie("anuj")
print(driver.get_cookies())