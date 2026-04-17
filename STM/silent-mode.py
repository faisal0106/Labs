from selenium import webdriver
from selenium.webdriver.common.by import By
o = webdriver.ChromeOptions()
o.add_argument("--headless=new")
d = webdriver.Chrome(options=o)
d.get("https://the-internet.herokuapp.com/login")
d.find_element(By.ID,"username").send_keys("tomsmith")
d.find_element(By.ID,"password").send_keys("SuperSecretPassword!")
d.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
print("PASS" if "secure area" in d.page_source else "FAIL")
d.quit()
