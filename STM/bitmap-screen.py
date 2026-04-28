from selenium import webdriver
import time as t
from PIL import Image
import pyautogui
print("Bitmap checkpoint for screen area")
driver = webdriver.Chrome()
driver.get("https://www.python.org")
t.sleep(5)
img = pyautogui.screenshot(region=(0, 0, 400, 300))
img.save("screen.png")
try:
    base = Image.open("base_screen.png")
    curr = Image.open("screen.png")
    if base.tobytes() == curr.tobytes():
        print("Screen Area Matched")
        print("Test Passed")
    else:
        print("Screen Area Not Matched")
        print("Test Failed")
except:
    img.save("base_screen.png")
    print("Baseline created, run again")
driver.quit()
