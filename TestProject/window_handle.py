from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
s = Service(r"C:\Users\anujp\PycharmProjects\TestProject\Browsers\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://www.selenium.dev/documentation/about/")
driver.find_element(By.XPATH, "/html/body/div/footer/div/div/div[1]/ul/li[3]/a/i").click()
print(driver.current_window_handle) # this command gives the hexadesimal number(CDwindow-CD89EEB86A65D3927B4AFEEA09D5506A) of current windows
handle = driver.window_handles

for i in handle:
    driver.switch_to.window(i)
    print(driver.title)
    if driver.title == "About this documentation | Selenium":
        driver.close()


# current_window_handle --- parent
# windows_handles --- child handle ( this command is used for handle windows )
# driver.close() is used to close the current window while driver.quite() is used for closing all the tabs.

