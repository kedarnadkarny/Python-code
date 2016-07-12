from PIL import Image
import os

list = os.listdir("path") # dir is your directory path
number_files = len(list)
print(number_files)

size = 150, 150

for filename in os.listdir("path"):
    oldImage = Image.open("path\%s" % filename)
    print("path\%s" % filename)
    newImage = oldImage.resize(size, Image.ANTIALIAS)
    newImage.save("newpath\%s" % filename)
