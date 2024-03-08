from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Go to the Best Buy website
driver.get('https://www.bestbuy.ca/')

# Wait for demonstration purposes
time.sleep(5)

# Element:1 Find the account button and click it
account_button = driver.find_element("xpath",
                                     "/html/body/div[1]/div/div[3]/header/div/div/div[1]/div[2]/div[2]/div[1]/a")
account_button.click()

# Wait for demonstration purposes
time.sleep(5)

# Element:2 Find the email input field and enter the email address
email_input = driver.find_element("xpath",
                                  "/html/body/div[1]/div/div[3]/div/div/div/div[1]/div/div/form/fieldset/div[1]/div/div[1]/div/input")
email_input.send_keys("shubamkumaraug@gmail.com")

# Wait for demonstration purposes
time.sleep(3)

# Element:3 Find the password input field and enter the password
password_input = driver.find_element("xpath",
                                     "/html/body/div[1]/div/div[3]/div/div/div/div[1]/div/div/form/fieldset/div[2]/div/div[1]/div/input")
password_input.send_keys("Shubham@12")

# Wait for demonstration purposes
time.sleep(3)

# Element:4 Find the 'Sign In' button and click it
signin_button = driver.find_element("xpath", "/html/body/div[1]/div/div[3]/div/div/div/div[1]/div/div/form/div/button")
signin_button.click()

# Wait for the page to load
time.sleep(5)

# Close the browser
driver.quit()
