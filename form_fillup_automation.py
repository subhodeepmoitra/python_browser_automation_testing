# importing the modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# using chrome driver
driver = webdriver.Chrome('/home/subhodeep/Documents/python/automation_testing/chromedriver')

# web page url
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
driver.maximize_window()

# select class name where is input box are present
element = driver.find_elements(By.CLASS_NAME, "text_field")

# find number of input box
print(len(element))

# fill value in input box
driver.find_element_by_xpath('//*[@id="RESULT_TextField-1"]').send_keys("Subhodeep")
driver.find_element_by_xpath('//*[@id="RESULT_TextField-2"]').send_keys("Moitra")
driver.find_element_by_xpath('//*[@id="RESULT_TextField-3"]').send_keys("9007670235")
driver.find_element_by_xpath('//*[@id="RESULT_TextField-4"]').send_keys("India")
# check status
x = driver.find_element_by_xpath('//*[@id="RESULT_TextField-1"]').is_displayed()
print(x)
#driver.close()
