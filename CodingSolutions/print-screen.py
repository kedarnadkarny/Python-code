import time
from PIL import ImageGrab
import os

new = 0
content_list = []

for content in os.listdir('C:\\Users\\DnG\\Desktop\\screenshot'):
    path = 'C:\\Users\\DnG\\Desktop\\screenshot\\%s'%content
    if os.path.isfile(path):
        content_list.append(os.path.basename(path)[0])

current = max(content_list)
current = int(current)
print(current)
new = current + 1
new = str(new)
new += ".jpg"

time.sleep(2)
ImageGrab.grab().save("C:\\Users\\DnG\\Desktop\\screenshot\\%s"%new)