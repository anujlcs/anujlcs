from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait, expected_conditions

service = Service(r"C:\Users\anujp\PycharmProjects\TestProject\Browsers\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://www.selenium.dev/documentation/webdriver/browser/alerts/")
driver.find_element(By.LINK_TEXT, "See an example alert").click()
# Wait for the alert to be displayed and store it in a variable
alert = wait.until(expected_conditions.alert_is_present())

# Store the alert text in a variable
text = alert.text

# Press the OK button
alert.accept()

