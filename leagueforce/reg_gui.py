from tkinter import *
import numpy as np
import cv2
import os
import csv
wn=Tk()
wn.title("Beat Management")
wn.geometry("1000x400")

def read_face():
        fname=(tb.get())

#name=input("Enter the file name")
        path = '/home/tarunraj/hackathon/training-data/'
        os.chdir(path)

        a=os.mkdir(fname)
        print(a)
#print(a)
        cap = cv2.VideoCapture(0)
        count=0
        while(True):
    # Capture frame-by-frame
                ret, image = cap.read()
                print(count)
    # Our operations on the frame come here
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

                path = '/home/tarunraj/hackathon/training-data/'+fname+'/'
                c=path+"image"+str(count)+".jpg"
   # print(c)
    #print(image)
                cv2.imwrite(c, image) 
    # Display the resulting frame
                cv2.imshow('Image',gray)
                count+=1
                if count==200:
                            break
                if cv2.waitKey(1) & 0xFF == ord('q'):
                            break
        cap.release()
        cv2.destroyAllWindows()

        

def sto():
        fname=(tb.get())
        name=(tb1.get())
        print(name)
        d=[fname,name]
        with open('people.csv', 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(d)

        csvFile.close()
        read_face()


def close():
        wn.destroy()




lb=Label(wn,text="Registration of constable face",font=('times new roman',30)).pack()
lb1=Label(wn,text="Enter Constable ID")
lb1.place(x=320,y=55)

tb=Entry(wn,width=20)
tb.place(x=460,y=54)

lb2=Label(wn,text="Enter constable name")
lb2.place(x=320,y=100)

tb1=Entry(wn,width=20)
tb1.place(x=460,y=99)

b1=Button(wn,text="Record",command=sto)
b1.place(x=370,y=150)

b2=Button(wn,text="Close",command=close)
b2.place(x=530,y=150)

wn.mainloop()
