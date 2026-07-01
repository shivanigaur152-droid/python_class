from datetime import datetime
# import time
current=datetime.now().today()
print(current)
import pyautogui
import time
time.sleep(5)
for i in range(10):
  pyautogui.typewrite(" my name is shivani and I'm data scientist ",interval=0.12)
  