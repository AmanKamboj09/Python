import cv2
import numpy as np
img = cv2.imread('Madhuri.jpg')

cv2.imshow('ORIGIONAL IMAGE', img)
cv2.waitKey(0)

Trans_Img = cv2.transpose(img)
cv2.imshow("Tranpose", Trans_Img)
cv2.waitKey(0)

cv2.destroyAllWindows()
