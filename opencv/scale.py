from cv2 import cv2
import numpy as np 
image = cv2.imread('bib.png')
print(image.shape)

image2 = cv2.resize(image, None,fx=3, fy=2, interpolation = cv2.INTER_CUBIC)
M = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(image2,M,(1050,1000))
dst = cv2.warpAffine(image,M,(1050,1000))
cv2.imshow('final',image2)
cv2.imshow('also',dst)
cv2.imshow('ha ha',image)
cv2.waitKey()