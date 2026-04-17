import pyautogui
import time
print("Recording in Analog mode.....")
time.sleep(4)
pyautogui.click(400,500)
pyautogui.write("echo Selenium python",interval =0.1)
pyautogui.press("enter")
print("Success")
