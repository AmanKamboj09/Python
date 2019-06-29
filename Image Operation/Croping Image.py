import cv2
import numpy as np

img = cv2.imread('Many_Faces.png')
cv2.imshow('ORIGIONAL IMAGE', img)
cv2.waitKey(0)

# x,y = 10,10
h,w = img.shape[:2]
print(h,w)
# x1,y1 = x+int(h/2), y+int(w/2)

cropped = img[50:300, 60:350]
# cropped = img[x:x1, y:y1]

cv2.imshow("Cropped", cropped)
cv2.waitKey(0)

cv2.destroyAllWindows()
