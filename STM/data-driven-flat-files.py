from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
print("Data Driven Test - Text File")
driver = webdriver.Chrome()
try:
    with open("sample.txt") as f:
        for i, line in enumerate(f, start=1):
            data = line.strip() or "default"
            print(f"\nTest Case {i}")
            print("Input:", data)
            driver.get("https://www.google.com")
            try:
                consent = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Accept')]"))
                )
                consent.click()
            except:
                pass
            search = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.NAME, "q"))
            )
            search.clear()
            search.send_keys(data)
            search.send_keys(Keys.RETURN)
            print("Search completed")
            time.sleep(2)

finally:
    driver.quit()
