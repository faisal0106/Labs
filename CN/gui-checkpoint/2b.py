from selenium import webdriver
from selenium.webdriver.common.by import By
import time as t
print("Gui checkpoint for single object/window")
driver = webdriver.Chrome()
driver.get("https://www.google.com")
search_box = driver.find_element(By.NAME, "q")
status = search_box.is_displayed()
t.sleep(5)
print("Object Displayed Status:", status)
if status:
    print("Object is visible")
    print("Test Passed")
else:
    print("Object not visible")
    print("Test Failed")
driver.quit()
