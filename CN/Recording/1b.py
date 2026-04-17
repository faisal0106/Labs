from selenium import webdriver 
from selenium.webdriver.common.by import By
import time as t
print("Recording in Context sensitive mode")
driver = webdriver.Chrome()
driver.get("https://www.google.com")
search_box = driver.find_element(By.NAME,"q")
search_box.send_keys("Selenium Python")
search_box.submit()
t.sleep(3) 
print("Success")
driver.quit()
