from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
s = Service(r"C:\Users\anujp\PycharmProjects\TestProject_2\Browser\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://youtube.com")
time.sleep(2)

# search_box
text = driver.find_element(By.NAME, "search_query")
"""text = driver.find_element(By.XPATH, "//*[@id='search']")"""
text.click()
time.sleep(1)

text.send_keys("code with harry")
time.sleep(1)
# search_button_click
driver.find_element(By.XPATH, "//*[@id='search-icon-legacy']").click()
time.sleep(2)

# video click
video = driver.find_element(By.PARTIAL_LINK_TEXT, "Fonts & Sizing : Tailwind Tutorial #4")
video.click()
time.sleep(2)

# like
like = driver.find_element(By.XPATH, "//*[@id='top-level-buttons-computed']/ytd-toggle-button-renderer[1]/a")
like.click()
time.sleep(1)

# home
home = driver.find_element(By.ID, "start")
home.click()
time.sleep(2)

# news
news = driver.find_element(By.PARTIAL_LINK_TEXT, "News")
news.click()
time.sleep(2)

driver.refresh()
time.sleep(2)

driver.quit()

