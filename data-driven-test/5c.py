from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()
data = ["Python", "Selenium", "Automation"]
for i, item in enumerate(data, start=1):
    print(f"\nTest Case {i}")
    print("Input:", item)
    driver.get("https://www.google.com")
    search = WebDriverWait(driver, 10).until(
        lambda d: d.find_element(By.NAME, "q")
    )
    search.send_keys(item)
    search.submit()
    print("Search completed")
driver.quit()
