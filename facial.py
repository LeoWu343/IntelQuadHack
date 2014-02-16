import numpy as np
import cv2

face_cascades = []
face_cascades.append(cv2.CascadeClassifier('/opt/local/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml'))
face_cascades.append(cv2.CascadeClassifier('/opt/local/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml'))
face_cascades.append(cv2.CascadeClassifier('/opt/local/share/OpenCV/haarcascades/haarcascade_frontalface_alt_tree.xml'))
face_cascades.append(cv2.CascadeClassifier('/opt/local/share/OpenCV/haarcascades/haarcascade_frontalface_alt2.xml'))
eye_cascades = []
eye_cascades.append(cv2.CascadeClassifier('/opt/local/share/OpenCV/haarcascades/haarcascade_eye.xml'))
eye_cascades.append(cv2.CascadeClassifier('/opt/local/share/OpenCV/haarcascades/haarcascade_eye_tree_eyeglasses.xml'))

img = cv2.imread('mirror11.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = []
for face_cascade in face_cascades:
  faces.append(face_cascade.detectMultiScale(gray, 1.3, 5))
for stuff in faces:
  for (x,y,w,h) in stuff:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
