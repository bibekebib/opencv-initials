from colour import Color
from cv2 import cv2
import numpy as np 
a= input('enter a color=')
b = Color(a)
c = b.rgb
d = tuple(255*x for x in c)
e = d[::-1]

print(d)
#print(list(d))
cap = cv2.VideoCapture(0)
while(1):

    _, img = cap.read()
    hsl = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    green = np.uint8([[list(e)]])
    hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
    print (hsv_green)
    f = hsv_green[0][0][0]
    if f>10:
        lower = np.array([f-10,50,50])
    else:
        lower = np.array([f,50,50])  
    upper = np.array([f+10,255,255])
    colors = cv2.inRange(hsl, lower,upper)
    kernal = np.ones((5,5), "uint8")
    blue = cv2.dilate(colors, kernal)
    res = cv2.bitwise_and(img, img, mask = colors)
    contours,_=cv2.findContours(colors,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contours in enumerate(contours):
        area = cv2.contourArea(contours)
        if(area>300):
            #cv2.drawContours(img, contours, -1, (0,255,0),2)
            x,y,w,h =cv2.boundingRect(contours)
            img = cv2.rectangle(img,(x,y), (x+w,y+h),(20,20,200),2)
            #img = np.copy(img)
            img= cv2.flip(img, 1)
    cv2.imshow('original', img)
    cv2.imshow(a, res)
    if cv2.waitKey(10) & 0xFF == 27:
                cap.release()
                cv2.destroyAllWindows()
                break
