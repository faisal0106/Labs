from selenium import webdriver
from selenium.webdriver.common.by import By
import time as t
from PIL import Image
print("Bitmap checkpoint for Object/ Window......")
driver = webdriver.Chrome()
driver.get("https://python.org")
element = driver.find_element(By.CLASS_NAME,"python-logo")
element.screenshot("obj.png")
t.sleep(5)
try:
    base = Image.open("base_obj.png")
    curr = Image.open("obj.png")
    if list(base.getdata()) == list(curr.getdata()):
        print("Object Matched")
        print("Test Passed")
    else:
        print("Not Matched")
        print("Test Failed")
except:
    element.screenshot("base_obj.png")
    print("Baseline Created , run again to compare")
driver.quit()
