import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.google.com')

driver.find_element(By.ID, 'lst-ib').send_keys('abc')
print driver.find_element(By.TAG_NAME, 'img').get_attribute('src')

print driver.find_element(By.NAME, 'btnK').get_attribute('value')
print driver.find_element(By.NAME, 'btnI').get_attribute('value')

driver.find_element(By.NAME, 'btnK').click()
#driver.find_element(By.LINK_TEXT, 'ABC Home Page - ABC.com').click()
driver.find_element(By.PARTIAL_LINK_TEXT, 'ABC Home Page').click()

driver.find_element(By.XPATH, "//div[@id = 'hplogo']").click()

time.sleep(5)
driver.close()
