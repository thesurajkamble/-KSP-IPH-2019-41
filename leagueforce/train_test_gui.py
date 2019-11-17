from tkinter import *
import numpy as np
import cv2
import os

from PIL import Image, ImageTk
wn=Tk()
wn.title("Beat Management")
wn.geometry("1000x600")


def train():
        import face_rec_new

def close():
        wn.destroy()


lb=Label(wn,text="Training Using Images",font=('times new roman',30)).pack()
'''lb1=Label(wn,text="Enter :wq
 name")
lb1.place(x=280,y=55)

tb=Entry(wn,width=20)
tb.pack()'''
#import tkinter as tk

#window = tk.Tk()
'''image = Image.open('images.jpeg')
photo_image = ImageTk.PhotoImage(image)
label = Label(wn, image = photo_image)
label.pack()'''
#window.mainloop()

b1=Button(wn,text="Train And Test",command=train)
b1.place(x=400,y=90)
b2=Button(wn,text="Close",command=close)
b2.place(x=530,y=90)
wn.config(bg='grey')
wn.mainloop()

