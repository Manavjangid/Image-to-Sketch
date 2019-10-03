# modules imported
from PIL import Image
import numpy
import pyautogui
import time

# opening Image
img=Image.open("C:\\Users\\admin\\Desktop\\New folder\\test.jpg")

# getting size
a=img.size

# resizing Image
cs=int(100*(a[0]/a[1]))
rs=100
img2=img.resize((cs,rs),3)

# converting to black and white
img2=img2.convert('L')
bw = img2.point(lambda x: 0 if x<128 else 255, '1')

# converting to 2d array
img_array=numpy.array(bw)
array_attributes=img_array.shape

# working with gui
pyautogui.PAUSE=0.0001
screenWidth, screenHeight = pyautogui.size()
pyautogui.moveTo(520,740)
pyautogui.click()
time.sleep(3)
pyautogui.moveTo(350,65)
pyautogui.click()
pyautogui.moveTo(20,160)

# image to sketch
# adding border to image
c=20
r=160
while c<=cs+20:
    pyautogui.click()
    c+=1
    pyautogui.moveTo(c,r)
while r<=rs+160:
    pyautogui.click()
    r+=1
    pyautogui.moveTo(c,r)
while c>=20:
    pyautogui.click()
    c-=1
    pyautogui.moveTo(c,r)
while r>=160:
    pyautogui.click()
    r-=1
    pyautogui.moveTo(c,r)

    
# sketching the image
f_rc=[]
for i in range(array_attributes[0]):
    for j in range(array_attributes[1]):
        if (img_array[i][j]==False):
            f_rc.append([j,i])
for i in f_rc:
    pyautogui.moveTo(20+i[0],160+i[1])
    pyautogui.click()
bw.show()