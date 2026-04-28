from selenium import webdriver
from selenium.webdriver.common.by import By
import time
print("-----Gui Checkpoint for Single Property------")
driver = webdriver.Chrome()
driver.get("https://www.google.com")
actual_title = driver.title
expected_title = "Google"
assert actual_title == expected_title
time.sleep(5)
print("Expected Title: ",expected_title)
print("Actual Title: ",actual_title)
if (expected_title == actual_title):
	print("Expected Title = Actual Title")
	print("Test Passed")
else:
	print("Test Failed")
driver.quit()
