from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

chrome_driver = webdriver.Chrome('/home/subhodeep/Documents/python/automation_testing/chromedriver')
chrome_driver.get("https://www.technoindiahooghly.org/")
chrome_driver.implicitly_wait(20)
chrome_driver.maximize_window()
time.sleep(5)
chrome_driver.find_element_by_xpath("/html/body/table/tbody/tr[1]/td[2]/table/tbody/tr[1]/td[3]/table/tbody/tr[1]/td[1]/div/a/img").click()
WebDriverWait(chrome_driver, 5)
chrome_driver.find_element_by_xpath('/html/body/table/tbody/tr[4]/td/table/tbody/tr[4]/td/form/table/tbody/tr[2]/td[2]/input').send_keys("15201219082")

#chrome_driver.close()