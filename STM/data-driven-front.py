from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
data = ["Python", "Selenium", "Automation"]
for i, item in enumerate(data, start=1):
    print(f"\nTest Case {i}")
    print("Input:", item)
    driver.get("https://www.google.com")
    search = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "q"))
    )
    search.clear()
    search.send_keys(item)
    search.send_keys(Keys.RETURN)
    print("Search completed")
driver.quit()
