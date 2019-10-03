# modules imported
from PIL import Image
import numpy
import pyautogui
import time
import sys

# opening Image
# you can add your image path
img=Image.open(r"C:\Users\admin\Desktop\New folder\test.jpg")

# getting size
a=img.size

# resizing Image
img2=img.resize((int(20*(a[0]/a[1])),20),3)

# converting to black and white
img2=img2.convert('L')
bw = img2.point(lambda x: 0 if x<128 else 255, '1')

# converting to 2d array
img_array=numpy.array(bw)
array_attributes=img_array.shape

# working with gui
pyautogui.PAUSE=0.001
screenWidth, screenHeight = pyautogui.size()
pyautogui.moveTo(520,740)
pyautogui.click()
time.sleep(3)
pyautogui.moveTo(330,60)
pyautogui.click()
r=160
r1=160
c=20
c1=20
pyautogui.moveTo(c,r)


# sketching the Image
for i in range(array_attributes[0]):
    c1=c
    for j in range(array_attributes[1]):
        if (img_array[i][j]==False):
            pyautogui.click()
        c1+=1
        pyautogui.moveTo(c1,r1)
    r1+=1
    pyautogui.moveTo(c,r1)
bw.show()