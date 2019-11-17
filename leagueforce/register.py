import numpy as np`
import cv2
import os
fname=input("Enter the name of the student")

#name=input("Enter the file name")
path = '/home/tarunraj/Image/'
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
    
    path = '/home/tarunraj/Image/'+fname+'/'
    c=path+"image"+str(count)+".jpg"
   # print(c)
    #print(image)
    cv2.imwrite(c, image) 
    # Display the resulting frame
    cv2.imshow('Image',gray)
    count+=1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
