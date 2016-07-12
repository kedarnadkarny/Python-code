from PIL import Image
import os

list = os.listdir("C:\pypro") # dir is your directory path
number_files = len(list)
print(number_files)

for filename in os.listdir("C:\pypro\granite-samples-2"):
    oldImage = Image.open("C:\pypro\granite-samples-2\%s"%filename)
    print("C:\pypro\granite-samples-2\%s"%filename)
    newImage = oldImage.crop((0,0,300,300))
    newImage.save("C:\pypro\granite-samples-2-CROPPED\%s"%filename)