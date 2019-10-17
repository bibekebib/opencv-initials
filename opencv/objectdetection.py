from colour import Color
from cv2 import cv2
import numpy as np 
a= input('enter a color=')
b = Color(a)
c = b.rgb
d = tuple(255*x for x in c)
e = d[::-1]
print(e)