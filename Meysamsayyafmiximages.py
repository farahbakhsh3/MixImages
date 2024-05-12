import cv2
import numpy as np

original_image = cv2.imread("main.jpg")
logo = cv2.imread("2.jpg")

rows, cols, channels = logo.shape
roi = original_image[0:rows, 0:cols]
result = cv2.addWeighted(roi, 1, logo, 1, 0)
original_image[0:rows, 0:cols] = result

cv2.imwrite('final_image.jpg', original_image)
