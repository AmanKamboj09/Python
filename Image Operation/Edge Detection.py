#Edge Detection
import cv2
import numpy as np

img = cv2.imread("Many_Faces.png",0)

cv2.imshow('Origional Image', img)
cv2.waitKey(0)
height,width = img.shape

laplacian = cv2.Laplacian(img, cv2.CV_64F)
cv2.imshow('Laplacian Image',laplacian)
cv2.waitKey(0)

#Canny Edge detection uses gradiant values as thresholds
canny = cv2.Canny(img, 20, 170)
cv2.imshow('Canny Edge', canny)
cv2.waitKey(0)

cv2.destroyAllWindows()
