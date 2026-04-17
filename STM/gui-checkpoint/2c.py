from selenium import webdriver
import time as t
print("Gui checkpoint for multiple properties")
driver = webdriver.Chrome()
driver.get("https://www.google.com")
actual_title = driver.title
actual_url = driver.current_url
expected_title = "Google"
expected_url_part = "google"
assert actual_title == expected_title
assert expected_url_part in actual_url
t.sleep(5)
print("Expected title: ", expected_title)
print("Actual title: ", actual_title)
print("Current URL: ", actual_url)
if (expected_title == actual_title and expected_url_part in actual_url):
    print("All conditions satisfied")
    print("Test Passed")
else:
    print("Test Failed")
driver.quit()
