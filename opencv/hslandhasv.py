from cv2 import cv2
import numpy as np 
import webcolors

dict = {'red':[0,255,0], 'green':[0,0,255],'blue':[255,0,0]}
color = input()
if color in dict.keys():
    print(color)
    print(dict[color])
    wow = np.uint8([[dict[color]]])
    hsv_green = cv2.cvtColor(wow,cv2.COLOR_BGR2HSV)
    print (hsv_green)
else:
    print ('color out of dict')