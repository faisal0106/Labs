from selenium import webdriver
from selenium.webdriver.common.by import By
print("Data Driven Test using Dynamic Input.....")
driver = webdriver.Chrome()
driver.get("https://www.google.com")
data = input("Enter search text: ")
print("Entering data:", data)
driver.find_element(By.NAME, "q").send_keys(data)
driver.find_element(By.NAME, "q").submit()
print("Search executed successfully")
print("Test Completed")
driver.quit()
