import shutil
import os

#shutil.copy2('C:\pypro\img.png','C:\pypro\img2.png')

for filename in os.listdir("C:\pypro\shot"):
    if os.path.isdir("C:\pypro\shot\%s"%filename):
        continue
    else:
        print("File copied", filename)
