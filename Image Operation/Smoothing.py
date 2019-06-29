import cv2
import numpy as np
img = cv2.imread('Madhuri.jpg')

cv2.imshow('ORIGIONAL IMAGE', img)
cv2.waitKey(0)
# Craeting 3x3 kernel
blur = cv2.blur(img,(3,3))

cv2.imshow("Blur Image", blur)
cv2.waitKey(0)

Gaussin = cv2.GaussianBlur(img, (7,7),0)
cv2.imshow("GaussianBlur Image", blur)
cv2.waitKey(0)

Median = cv2.medianBlur(img, 5)
cv2.imshow("Median Blur", Median)
cv2.waitKey(0)
Biletral = cv2.bilateralFilter(img, 9,75,75)
cv2.imshow("Biletral Blur", Biletral)
cv2.waitKey(0)

cv2.destroyAllWindows()