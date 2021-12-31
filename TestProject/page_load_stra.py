from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
service = Service(r"C:\Users\anujp\PycharmProjects\TestProject\Browsers\chromedriver.exe")
options = Options()
#options.page_load_strategy = 'normal'
options.page_load_strategy = 'eager'
#river = webdriver.Chrome(options=options)
driver = webdriver.Chrome(service=service,options=options)

driver.maximize_window()
driver.get("https://www.google.com")