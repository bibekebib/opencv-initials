from cv2 import cv2
import numpy as np 
cap = cv2.VideoCapture(0)
while(1):
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = face.detectMultiscale()