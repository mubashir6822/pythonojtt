from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
service_obj=Service("C:/udayme/seleniumcourse/chromedriver")
driver=webdriver.Chrome(service=service_obj)

driver.get("https://www.google.com/maps")
time.sleep(2)
driver.find_element(By.XPATH,"//button[@id='hArJGc']/img").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[@id='omnibox-directions']//div[@role='list']/div[1]/div[2]//div[@role='combobox']/input[@class='tactile-searchbox-input']").send_keys('chennei')
driver.find_element(By.XPATH,"//div[@id='omnibox-directions']//div[@role='list']/div[2]/div[2]//div[@role='combobox']/input[@class='tactile-searchbox-input']").send_keys('bangalore')
driver.find_element(By.XPATH,"//div[@id='omnibox-directions']//div[@role='list']/div[2]/div[2]/button[@class='mL3xi']").click()
time.sleep(10)
driver.close()
