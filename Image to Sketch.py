# modules imported
import tkinter as tk
from PIL import Image
import pyautogui
import time
import subprocess
import numpy


root=tk.Tk()
bul=tk.BooleanVar()
# Class that perform all the function on an Image
class functionality():
    def __init__(self):
        pass

    def processing(self,path,base_size,border):
        # opening Image
        img=Image.open(path)
        # getting size
        a=img.size

        # resizing Image
        cs=int(base_size*(a[0]/a[1]))
        rs=base_size
        img2=img.resize((cs,rs),3)

        # converting to black and white
        img2=img2.convert('L')
        bw = img2.point(lambda x: 0 if x<128 else 255, '1')

        # converting to 2d array
        img_array=numpy.array(bw)
        array_attributes=img_array.shape

        # working with GUI
        pyautogui.PAUSE=0.01
        # opening paint
        subprocess.call(["cmd", "/c", "start", "/max", "C:\\Windows\\system32\\mspaint.exe"])
        time.sleep(3)

        # making border for Sketch
        if border==1:
            pyautogui.moveTo(350,65)
            pyautogui.click()
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

        # Image to Sketch
        pyautogui.moveTo(240,65)
        pyautogui.click()
        f_rc=[]
        for i in range(array_attributes[0]):
            for j in range(array_attributes[1]):
                if (img_array[i][j]==False):
                    f_rc.append([j,i])
        for i in f_rc:
            pyautogui.moveTo(20+i[0],160+i[1])
            pyautogui.click()
        bw.show()

# Class that build UI and all input taken here
class Widget(functionality):
    def __init__(self):
        global bul
        global root
    
    def frame(self):
        no=tk.IntVar() #used to store Checkbutton value
        l=[] #used to store all 3 inputs
        # function called when button is clicked and is used to store all values to a list
        def values():
            l.clear()
            l.append(str(tf1.get()))
            l.append(int(tf2.get()))
            l.append(int(no.get()))
            functionality.processing(self,l[0],l[1],l[2])#this is calling function from other class and sending inputs           
            bul.set(False)# part of input taking mechanism

        # calling all the widgets
        l1=tk.Label(text="Enter Image Path")
        tf1=tk.Entry()
        l2=tk.Label(text="Enter Base Size")
        tf2=tk.Entry()
        cb1=tk.Checkbutton(text="Border",variable=no)
        b1=tk.Button(text="Start",command=values)

        # setting layout from the widgets
        l1.grid(row=0)
        tf1.grid(row=0,column=1)
        l2.grid(row=1)
        tf2.grid(row=1,column=1)
        cb1.grid(row=2,columnspan=2)
        b1.grid(row=3,columnspan=2)

        bul.set(True)# part of input taking mechanism
        root.wait_variable(bul)# part of input taking mechanism
        
        
root.title("Image to Sketch")
w=Widget()
w.frame()
root.mainloop()