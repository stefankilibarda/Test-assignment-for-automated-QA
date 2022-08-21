import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# initialize webdrive
driver = webdriver.Chrome('C:/Program Files (x86)/chromedriver.exe')

# Opens the URL and maximizes the browser window
driver.get('https://www.saucedemo.com/')
driver.maximize_window()
time.sleep(2)

# enter credentials
# enter username
username = driver.find_element(By.XPATH, '//*[@id="user-name"]')
username.click()
username.send_keys('standard_user')

# enter password
password = driver.find_element(By.XPATH, '//*[@id="password"]')
password.click()
password.send_keys('secret_sauce')
time.sleep(1)

# press login button
driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
time.sleep(2)

# add product to cart
driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
time.sleep(1)

# go to cart to verify item is added
driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
print('First item added to shopping cart')
time.sleep(3)

# assert correct item is added to cart
item1 = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')
assert item1.text == 'Sauce Labs Backpack'
print('First item verified')
time.sleep(2)

# continue shopping
driver.find_element(By.XPATH, '//*[@id="continue-shopping"]').click()
time.sleep(2)

# open another item's details page
driver.find_element(By.XPATH, '//*[@id="item_0_title_link"]/div').click()
time.sleep(2)

# add second item to shopping cart
driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
print('Second item added to shopping cart')
time.sleep(2)

# go to shopping cart and verify two items in shopping cart
driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
time.sleep(2)
item1 = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')
assert item1.text == 'Sauce Labs Backpack'
print('First item verified')
time.sleep(2)
item2 = driver.find_element(By.XPATH, '//*[@id="item_0_title_link"]/div')
assert item2.text == 'Sauce Labs Bike Light'
print('Second item verified')
time.sleep(2)

# remove first item from shopping cart
removeFirst = driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-backpack"]').click()

# assert correct item is present in the shopping cart
item2 = driver.find_element(By.XPATH, '//*[@id="item_0_title_link"]/div')
assert item2.text == 'Sauce Labs Bike Light'
print('Correct item is present')
time.sleep(2)

# proceed to checkout page
checkout = driver.find_element(By.XPATH, '//*[@id="checkout"]')
checkout.click()
time.sleep(2)

# populate checkout form
firstName = driver.find_element(By.XPATH, '//*[@id="first-name"]')
firstName.click()
firstName.send_keys('TestFirstName')
time.sleep(1)

lastName = driver.find_element(By.XPATH, '//*[@id="last-name"]')
lastName.click()
lastName.send_keys('TestLastName')
time.sleep(1)

postalCode = driver.find_element(By.XPATH, '//*[@id="postal-code"]')
postalCode.click()
postalCode.send_keys('23456')
time.sleep(1)

# complete order
driver.find_element(By.XPATH, '//*[@id="continue"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="finish"]').click()
time.sleep(1)

# verify order is successful
successMessage = driver.find_element(By.XPATH, '//*[@id="checkout_complete_container"]/h2')
assert successMessage.text == 'THANK YOU FOR YOUR ORDER'
print('Shopping successful!')

# close automated browser
driver.close()
