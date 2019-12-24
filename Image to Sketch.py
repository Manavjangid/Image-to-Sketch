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

    def processing(self,path,base_size,border):
        def start():
            s_root.destroy()
            # working with GUI
            pyautogui.PAUSE=0.01

            # opening paint
            subprocess.call(["cmd", "/c", "start", "/max", "C:\\Windows\\system32\\mspaint.exe"])
            time.sleep(3)

            # calculating center point to Draw
            sr=int(((550-rs)/2)+143)
            sc=int(((1347-cs)/2)+5)
            
            # making border for Sketch
            if border==1:
                pyautogui.moveTo(350,65)
                pyautogui.click()
                c=sc
                r=sr
                while c<=cs+sc:
                    pyautogui.click()
                    c+=1
                    pyautogui.moveTo(c,r)
                while r<=rs+sr:
                    pyautogui.click()
                    r+=1
                    pyautogui.moveTo(c,r)
                while c>=sc:
                    pyautogui.click()
                    c-=1
                    pyautogui.moveTo(c,r)
                while r>=sr:
                    pyautogui.click()
                    r-=1
                    pyautogui.moveTo(c,r)

            # Image to Sketch
            pyautogui.moveTo(240,65)
            pyautogui.click()
            for i in f_rc:
                pyautogui.moveTo(sc+i[0],sr+i[1])
                pyautogui.click()
            # bw.show()

            # creating message dialog box
            t_root=tk.Tk()
            t_root.title("Attension!!")

            la=tk.Label(t_root,text="      ")
            lb=tk.Label(t_root,text="      ")
            lc=tk.Label(t_root,text="      ")

            l1=tk.Label(t_root,text="Done!!")
            ld=tk.Label(t_root,text="      ")
            b1=tk.Button(t_root,text="OK",command=t_root.destroy)

            la.grid(row=0,column=0)
            lb.grid(row=0,column=1)
            lc.grid(row=0,column=2)

            l1.grid(row=1,column=0)
            ld.grid(row=1,column=1)
            b1.grid(row=1,column=2)

            t_root.call('wm', 'attributes', '.', '-topmost', '1')

            t_root.geometry("100x70+100+300")
            t_root.mainloop()

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

        # calculating no. of points to be printed
        f_rc=[]
        for i in range(array_attributes[0]):
            for j in range(array_attributes[1]):
                if (img_array[i][j]==False):
                    f_rc.append([j,i])
        
        if (rs<=530 and cs<=1325):
            # calculating aproximate time to Sketch an Image
            aprox_time=3.2+(0.02*(2*(cs+rs)))+(0.02*len(f_rc))

            # creating message dialog box
            s_root=tk.Tk()        
            s_root.title("Attension")

            la=tk.Label(s_root,text="           ")
            l1=tk.Label(s_root,text="It will take Approx.") 
            l2=tk.Label(s_root,text=f"{round(aprox_time/60,0)+round(aprox_time%60/100,2):.2f}Min to make this Sketch.")
            lb=tk.Label(s_root,text="           ")

            b1=tk.Button(s_root,text="Start",command=start)
            b2=tk.Button(s_root,text="Exit",command=s_root.destroy)

            la.grid(row=0)
            l1.grid(row=1,column=0)
            l2.grid(row=1,column=1)
            lb.grid(row=2)
            b1.grid(row=3,column=0)
            b2.grid(row=3,column=1)

            s_root.call('wm', 'attributes', '.', '-topmost', '1')
            s_root.geometry("280x100+100+300")
            s_root.mainloop()
        else:
            # creating message dialog box
            f_root=tk.Tk()
            f_root.title("Attension!!")

            la=tk.Label(f_root,text="      ")
            lb=tk.Label(f_root,text="      ")

            l1=tk.Label(f_root,text="Your Base Size is")
            l2=tk.Label(f_root,text="too Big to Draw!!")

            lc=tk.Label(f_root,text="      ")
            ld=tk.Label(f_root,text="      ")

            b1=tk.Button(f_root,text="OK",command=f_root.destroy)

            la.grid(row=0,column=0)
            lb.grid(row=0,column=1)

            l1.grid(row=1,column=0)
            l2.grid(row=1,column=1)

            lc.grid(row=2,column=0)
            ld.grid(row=2,column=1)

            b1.grid(row=3,columnspan=2)

            f_root.call('wm', 'attributes', '.', '-topmost', '1')
            f_root.geometry("190x100+100+300")
            f_root.mainloop()


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
        
root.geometry("230x100+300+300")
root.title("Image to Sketch")
w=Widget()
w.frame()
root.mainloop()