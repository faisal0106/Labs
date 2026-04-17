from selenium import webdriver
from selenium.webdriver.common.by import By
import time as t
print("Gui checkpoint for single property")
driver = webdriver.Chrome()
driver.get("https://www.google.com")
actual_title = driver.title
expected_title = "Google"
assert actual_title == expected_title
t.sleep(5)
print("Expected title: ", expected_title)
print("Actual title: ", actual_title)
if (expected_title == actual_title):
    print("Expected title = Actual Title")
    print("Test Passed")
else:
    print("Test Failed")
    


