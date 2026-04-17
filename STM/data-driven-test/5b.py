from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
with open("sample.txt") as f:
    for i, line in enumerate(f, start=1):
        data = line.strip() or "default"
        print(f"\nTest Case {i}")
        print("Input:", data)
        driver.get("https://www.google.com")
        driver.find_element(By.NAME, "q").send_keys(data)
        driver.find_element(By.NAME, "q").submit()
        print("Search completed")
driver.quit()
