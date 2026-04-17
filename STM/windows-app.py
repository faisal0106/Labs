import pyautogui
import time
import subprocess
subprocess.Popen(["gnome-calculator"])
time.sleep(3)  # wait for app to open
pyautogui.press('7')
pyautogui.press('+')
pyautogui.press('3')
pyautogui.press('enter')
time.sleep(1)
print("Executed: 7 + 3")
print("Result should be: 10 → VERIFY MANUALLY")
pyautogui.hotkey('alt', 'f4')
