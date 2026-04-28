import pyautogui as p
import time as t
print("-----Recording in Analog Mode-----")
t.sleep(4)
p.click(400,500)
p.write("echo Selenium Python",interval = 0.1)
p.press("enter")
print("Done...!")
