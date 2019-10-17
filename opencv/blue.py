import numpy  as np
from cv2 import cv2
cap = cv2.VideoCapture(0)
while (True):
    _, img = cap.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    yellow_lower = np.array([0,100,100], np.uint8)
    yellow_upper = np.array([10,255,255], np.uint8)
    yellow = cv2.inRange(hsv, yellow_lower, yellow_upper)
    kernal = np.ones((5,5), "uint8")
    blue = cv2.dilate(yellow, kernal)
    res = cv2.bitwise_and(img, img, mask=yellow)
    contours,hierarchy=cv2.findContours(yellow,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contours in enumerate(contours):
        area = cv2.contourArea(contours)
        if(area>300):
            x,y,w,h =cv2.boundingRect(contours)
            img = cv2.rectangle(img,(x,y), (x+w,y+h),(20,20,200),2)
            img= cv2.flip(img, 1)
    cv2.imshow('Yellow', res)
    cv2.imshow("color Tracking", img)
    if cv2.waitKey(10) & 0xFF == 27:
                cap.release()
                cv2.destroyAllWindows()
                break