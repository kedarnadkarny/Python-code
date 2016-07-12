from PIL import Image
import os

list = os.listdir("C:\\wamp\\www\\ajantamarbles\images\products\granite-samples-2") # dir is your directory path
number_files = len(list)
print(number_files)

size = 150, 150

for filename in os.listdir("C:\\wamp\\www\\ajantamarbles\images\products\granite-samples-2"):
    oldImage = Image.open("C:\\wamp\\www\\ajantamarbles\images\products\granite-samples-2\%s" % filename)
    print("C:\\wamp\\www\\ajantamarbles\images\products\granite-samples-2\%s" % filename)
    newImage = oldImage.resize(size, Image.ANTIALIAS)
    newImage.save("C:\wamp\www\\ajantamarbles\images\products\\thumbnail\%s" % filename)
