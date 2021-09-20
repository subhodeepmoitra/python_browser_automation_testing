from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/home/subhodeep/Documents/python/automation_testing/chromedriver')
driver.get("https://www.python.org")
print(driver.title)
