from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
service = Service(r"C:\Users\anujp\PycharmProjects\TestProject_2\Browser\chromedriver.exe")
driver = webdriver.Chrome(service = service)
driver.maximize_window()
# Hitting Url
driver.get("http://www.tutorialsninja.com/demo/")
time.sleep(2)

# click on phones & PAds
driver.find_element(By.LINK_TEXT, "Phones & PDAs").click()
time.sleep(2)

# click on iphone
driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div[2]/div/div[1]/a/img").click()
time.sleep(2)

#click on image
driver.find_element(By.XPATH, "//*[@id='content']/div[1]/div[1]/ul[1]/li[1]/a").click()
time.sleep(2)

#click on next image button
button=driver.find_element(By.XPATH, "/html/body/div[2]/div/button[2]")
for i in range(0,5):
    button.click()
    time.sleep(1)

# take screenshot
# driver.save_screenshot("E-scn.png")
driver.find_element(By.CLASS_NAME, "mfp-close").click()
# add quantity
"""quantity = driver.find_element(By.NAME, "quantity")
quantity.click()
time.sleep(1)
quantity.clear()
time.sleep(1)
quantity.send_keys("2")
# click on add to cart button
driver.find_element(By.ID, "button-cart").click()
time.sleep(2)"""

# hover on menu bar
action = ActionChains(driver)
laptop = driver.find_element(By.XPATH, "//*[@id='menu']/div[2]/ul/li[2]/a")
action.move_to_element(laptop).perform()
time.sleep(2)

#click on Show All Laptops & Notebooks
driver.find_element(By.LINK_TEXT, "Show All Laptops & Notebooks").click()

# scrolling screen
driver.execute_script("window.scrollBy (0,400)" , "")
time.sleep(2)

#click on laptop image
driver.find_element(By.XPATH, '//*[@id="content"]/div[4]/div[1]/div/div[1]/a/img').click()
time.sleep(2)

# clear date in date box
date = driver.find_element(By.NAME, "option[225]")
date.click()
time.sleep(2)
date.clear()
time.sleep(2)

# set new date
date.send_keys("10-1-2022")
time.sleep(2)

# click on add tp cart
driver.find_element(By.ID, "button-cart").click()
time.sleep(2)

#click item button
driver.find_element(By.XPATH, "//*[@id='cart']/button").click()

# checkout button
driver.find_element(By.XPATH, "//*[@id='cart']/ul/li[2]/div/p/a[2]").click()
time.sleep(2)

# guest button
driver.find_element(By.XPATH, "//*[@id='collapse-checkout-option']/div/div/div[1]/div[2]/label/input").click()
time.sleep(2)

# continue button
driver.find_element(By.ID, "button-account").click()



time.sleep(2)

first_name= driver.find_element(By.XPATH, "//*[@id='input-payment-firstname']")
first_name.click()
first_name.send_keys("Anuj")
time.sleep(2)

last_name= driver.find_element(By.ID, "input-payment-lastname")
last_name.click()
last_name.send_keys("pandey")
time.sleep(2)

email=driver.find_element(By.ID, "input-payment-email")
email.click()
email.send_keys("anujpandey05077@gmail.com")
time.sleep(2)

phone=driver.find_element(By.ID, "input-payment-telephone")
phone.click()
phone.send_keys("8115563192")
time.sleep(2)

address=driver.find_element(By.ID, "input-payment-address-1")
address.click()
address.send_keys("Babu Ram Sarraf Nagar")
time.sleep(2)

city=driver.find_element(By.ID, "input-payment-city")
city.click()
city.send_keys("Lucknow")
time.sleep(2)

code=driver.find_element(By.ID,"input-payment-postcode")
code.click()
code.send_keys("262701")
time.sleep(2)

country=driver.find_element(By.ID, "input-payment-country")
country.click()
time.sleep(2)

india=driver.find_element(By.XPATH, "//*[@id='input-payment-country']/option[107]")
india.click()
time.sleep(2)

state=driver.find_element(By.XPATH, "//*[@id='input-payment-zone']")
state.click()
time.sleep(2)

up=driver.find_element(By.XPATH, "//*[@id='input-payment-zone']/option[33]")
up.click()
time.sleep(2)

# continue button
driver.find_element(By.XPATH, "//*[@id='button-guest']").click()
time.sleep(2)

# step_4 continue button
driver.find_element(By.XPATH, "//*[@id='button-shipping-method']").click()
time.sleep(2)

# checkbox
driver.find_element(By.XPATH, "//*[@id='collapse-payment-method']/div/div[2]/div/input[1]").click()
time.sleep(2)

# step_5 continue button
driver.find_element(By.XPATH, "//*[@id='button-payment-method']").click()
time.sleep(2)

# step_6 confirm order
driver.find_element(By.XPATH, "//*[@id='button-confirm']").click()
time.sleep(10)
driver.quit()


