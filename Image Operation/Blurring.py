import cv2
import numpy as np

img = cv2.imread('Madhuri.jpg')
# print(img)
cv2.imshow('ORIGIONAL IMAGE', img)
cv2.waitKey(0)

# Creating 3x3 kernel
kernel_3x3 =np.ones((3,3),np.float32)/9
blurred = cv2.filter2D(img, -1,kernel_3x3)
cv2.imshow("Blurring 3x3", blurred)
cv2.waitKey(0)

kernel_5x5 =np.ones((5,5),np.float32)/25
blurred = cv2.filter2D(img, -1,kernel_5x5)
cv2.imshow("Blurring 5x5", blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()
