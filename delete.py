import pyautogui
import time
import random
import subprocess

# Step 1: Click at (501, 82)
pyautogui.click(501, 82)
time.sleep(0.7)

# Step 2: Type URL
pyautogui.write("https://github.com/codespaces/")
time.sleep(0.7)

# Step 3: Press Enter
pyautogui.press('enter')
time.sleep(10)

# Step 4: Perform random click in rectangular area (625, 230) to (832, 306)
x = random.randint(625, 832)
y = random.randint(230, 306)
pyautogui.moveTo(x, y, duration=random.uniform(0.2, 0.5))  # simulate natural movement
pyautogui.click()
time.sleep(random.uniform(0.5, 1))

# Step 5: Run scroll.py
subprocess.run(["python3", "scroll.py"])
time.sleep(0.5)

# Step 6: Run press.py
subprocess.run(["python3", "press.py"])
time.sleep(6)

# Step 7: Click at (97, 82)
pyautogui.click(97, 82)
time.sleep(7)

# Step 8: Run codespace.py
subprocess.run(["python3", "codespace.py"])
time.sleep(1)

# Step 9: Run boss.py
subprocess.run(["python3", "boss.py"])
