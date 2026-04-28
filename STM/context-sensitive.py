from selenium import webdriver
from selenium.webdriver.common.by import By
import time
print("-----Recording in Context-sensitive Mode-----")
driver = webdriver.Chrome()
driver.get("https://www.google.com")
search_box = driver.find_element(By.NAME,"q")
search_box.send_keys("Selenium Python")
search_box.submit()
time.sleep(5)
print("Search Completed.....!")
driver.quit()
