from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("/home/subhodeep/Documents/python/automation_testing/chromedriver")

driver.get("https://technocollegehooghly.org/studentportal/")
driver.maximize_window()

driver.find_element_by_xpath('/html/body/table/tbody/tr[4]/td/table/tbody/tr[4]/td/form/table/tbody/tr[2]/td[2]/input').send_keys("15201219082")
driver.implicitly_wait(10)
driver.find_element_by_xpath('/html/body/table/tbody/tr[4]/td/table/tbody/tr[4]/td/form/table/tbody/tr[3]/td[2]/input').send_keys("18072000")
driver.implicitly_wait(10)
driver.find_element_by_xpath('/html/body/table/tbody/tr[4]/td/table/tbody/tr[4]/td/form/table/tbody/tr[4]/td/input').click()
driver.implicitly_wait(30)
driver.back()

driver.close()