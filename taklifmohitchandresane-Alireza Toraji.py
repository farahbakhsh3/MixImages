import cv2 
import numpy as np

img1 = cv2.imread('ABC1.png')
img2 = cv2.imread('ABC2.png')

add = cv2.addWeighted(img1, 0.4 , img2 , 0.7 , 0)

cv2.imshow('ABC1',img1)
cv2.imshow('ABC2',img2)
cv2.imshow("add" , add )

cv2.waitKey(0)
cv2.destroyAllWindows