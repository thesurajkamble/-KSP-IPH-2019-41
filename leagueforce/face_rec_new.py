#import OpenCV module
import cv2
#import os module for reading training data directories and paths
import os
import numpy as np
import pandas as pd
import csv

present=[]

#there is no label 0 in our training data so subject name for index/label 0 is empty
subjects = [""]
print(subjects)

#name=[]
i=0
data=pd.read_csv("people.csv")
m=data['name']

print(len(m))
while(i<len(m)-1):
           subjects.append(m[i])
           #print(m[i])
           i+=1

#print(name)


#function to detect face using OpenCV
def detect_face(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    face_cascade = cv2.CascadeClassifier('opencv-files/haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=10)

    if len(faces) == 0:
        faceDet_two = cv2.CascadeClassifier("opencv-files/haarcascade_frontalface_alt2.xml")
        faces = faceDet_two.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10)
    elif len(faces) == 0:
        faceDet_three = cv2.CascadeClassifier("opencv-files/haarcascade_frontalface_alt.xml")
        faces = faceDet_three.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10)
    elif len(faces) == 0:
        faceDet_four = cv2.CascadeClassifier("opencv-files/haarcascade_frontalface_alt_tree.xml")
        faces = faceDet_four.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10)

    if len(faces) == 0:
        print("None of Faces Found")
        return None, None
    print("Total Faces Found", len(faces))
    
    #extract the face area
    for (x, y, w, h) in faces:
      cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
      print("in predict train face",w,":",h)
    #return only the face part of the image
    return gray[y:y+w, x:x+h], faces[0]


def detect_face_predict(img):
    #convert the test image to gray image as opencv face detector expects gray images
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    face_cascade = cv2.CascadeClassifier('opencv-files/haarcascade_frontalface_alt.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5);
    faceDet_two = cv2.CascadeClassifier("opencv-files/haarcascade_frontalface_alt2.xml")
    faces_two = faceDet_two.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(5, 5), flags=cv2.CASCADE_SCALE_IMAGE)
    faceDet_three = cv2.CascadeClassifier("opencv-files/haarcascade_frontalface_alt.xml")
    faces_three = faceDet_three.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(5, 5), flags=cv2.CASCADE_SCALE_IMAGE)
    faceDet_four = cv2.CascadeClassifier("opencv-files/haarcascade_frontalface_alt_tree.xml")
    faces_four = faceDet_four.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(5, 5), flags=cv2.CASCADE_SCALE_IMAGE)

    print("Faces Detected:",len(faces))

    if len(faces_four) > len(faces):
        faces=faces_four

    if len(faces_three) > len(faces):
        faces=faces_three

    if len(faces_two) > len(faces):
        faces=faces_two

    if len(faces) == 0:
        return None, None
		
    
    #under the assumption that there will be only one face,
    #extract the face area
    grays=[]
    for (x, y, w, h) in faces:
      print("in predict predict face",w,":",h)
      print("in predict predict face",x,":",y)
      cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
      grays.append(gray[y:y+h, x:x+h])
    
    #return only the face part of the image
    return grays, faces


def prepare_training_data(data_folder_path):
    
    #------STEP-1--------
    #get the directories (one directory for each subject) in data folder
    dirs = os.listdir(data_folder_path)
    
    #list to hold all subject faces
    faces = []
    #list to hold labels for all subjects
    labels = []
    
    #let's go through each directory and read images within it
    for dir_name in dirs:
        
        #our subject directories start with letter 's' so
        #ignore any non-relevant directories if any
        if not dir_name.startswith("s"):
            continue;
            
        #------STEP-2--------
        #extract label number of subject from dir_name
        #format of dir name = slabel
        #, so removing letter 's' from dir_name will give us label
        label = int(dir_name.replace("s", ""))
        
        #build path of directory containin images for current subject subject
        #sample subject_dir_path = "training-data/s1"
        subject_dir_path = data_folder_path + "/" + dir_name
        
        #get the images names that are inside the given subject directory
        subject_images_names = os.listdir(subject_dir_path)
        
        #------STEP-3--------
        #go through each image name, read image, 
        #detect face and add face to list of faces
        for image_name in subject_images_names:
            
            #ignore system files like .DS_Store
            if image_name.startswith("."):
                continue;
            
            #build image path
            #sample image path = training-data/s1/1.pgm
            image_path = subject_dir_path + "/" + image_name

            #read image
            image = cv2.imread(image_path)
            
            image=cv2.resize(image, (300, 400))
            #display an image window to show the image 
            cv2.imshow("Training on image...", cv2.resize(image, (400, 500)))
            cv2.waitKey(10)
            #detect face
            face, rect = detect_face(image)
            
            #------STEP-4--------
            #for the purpose of this tutorial
            #we will ignore faces that are not detected
            if face is not None:
                print(face.shape)
                #add face to list of faces
                faces.append(face)
                #add label for this face
                labels.append(label)
            else:
                
            
                cv2.destroyAllWindows()
                cv2.waitKey(1)
                cv2.destroyAllWindows()
    
    return faces, labels



print("Preparing data...")
faces, labels = prepare_training_data("training-data")
print("Data prepared")

#print total faces and labels
print("Total faces: ", len(faces))
print("Total labels: ", len(labels))

print("Total labels: ", labels)

face_recognizer = cv2.face.createLBPHFaceRecognizer()

#or use EigenFaceRecognizer by replacing above line with 
#face_recognizer = cv2.face.createEigenFaceRecognizer()

#or use FisherFaceRecognizer by replacing above line with 
#face_recognizer = cv2.face.createFisherFaceRecognizer()


#train our face recognizer of our training faces
face_recognizer.train(faces, np.array(labels))


#function to draw rectangle on image 
#according to given (x, y) coordinates and 
#given width and heigh
def draw_rectangle(img, rect):
    (x, y, w, h) = rect
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
#function to draw text on give image starting from
#passed (x, y) coordinates. 
def draw_text(img, text, x, y):
    cv2.putText(img, text, (x-13, y), cv2.FONT_HERSHEY_SIMPLEX,0.4, (0, 255, 0), 1,cv2.LINE_AA)


#this function recognizes the person in image passed
#and draws a rectangle around detected face with name of the 
#subject
def predict(test_img):
    print(test_img)
    #make a copy of the image as we don't want to chang original image
    img = test_img.copy()
    #detect face from the image
    img=cv2.resize(img,(128,128))
    faces, rects = detect_face_predict(img)
    #print(faces)
    labels=[]
    #predict the image using our face recognizer 
    i=0
    for face in (faces):
      print("Predicting Face",face)
      label, confidence = face_recognizer.predict(face)
      present.append(label)
      print(label,":",confidence)
    #get name of respective label returned by face recognizer
      label_text = subjects[label]
      print(label_text,":",confidence)
      labels.append(label_text)
    
    #draw a rectangle around face detected
      rect=rects[i]
      i=i+1
      draw_rectangle(img, rect)
    #draw name of predicted person
      draw_text(img, label_text, rect[0], rect[1]-5)
    
    return img

# In[10]:

print("Predicting images...")

#load test images
test_img1 = cv2.imread("test-data/ftest1.JPG")

#test_img2 = cv2.imread("test-data/img.jpg")

#test_img3 = cv2.imread("test-data/lok.JPG")

#perform a prediction
predicted_img1 = predict(test_img1)

#predicted_img2 = predict(test_img2)
#predicted_img3 = predict(test_img3)
print("Prediction complete")
l='Recognized Faces'
#display both images
cv2.imshow(l, cv2.resize(predicted_img1, (400, 500)))

i=0
com1=[]
data=pd.read_csv("people.csv")
m=data['name']
while(i<=len(present)-1):
            n=m[present[i]-1]
            i=i+1
            com1.append(n)
with open('attendance.csv', 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(com1)

#cv2.imshow(subjects[2], cv2.resize(predicted_img2, (400, 500)))

#cv2.imshow(subjects[3], cv2.resize(predicted_img3, (400, 500)))
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
cv2.destroyAllWindows()
