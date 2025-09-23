"""
AI Practical-14.py
Detect human faces from an image or camera feed using OpenCV's pre-trained Haar cascades. 

Run this command before executing the program: pip install opencv-python
Make sure you have the image (faces.jpeg) in the same folder as your script.

"""

import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
img = cv2.imread('faces.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
cv2.imshow('faces', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#  The program opens a window showing the image "faces.jpeg" with rectangles drawn around detected faces.