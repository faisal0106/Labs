from selenium import webdriver
from selenium.webdriver.common.by import By
o = webdriver.ChromeOptions()
o.add_argument("--headless=new")
d = webdriver.Chrome(options=o)
print("Launching browser in headless mode...")
d.get("https://the-internet.herokuapp.com/login")
print("Entering credentials...")
d.find_element(By.ID, "username").send_keys("tomsmith")
d.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
print("Submitting login form...")
d.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
result = "PASS" if "secure area" in d.page_source else "FAIL"
print("Checking login result...")
print("RESULT:", result)
d.quit()
print("Browser closed.")
