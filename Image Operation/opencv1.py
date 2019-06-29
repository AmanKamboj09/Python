import cv2

img = cv2.imread('Many_Faces.PNG',0)
# print(img)
cv2.imshow('Window1', img)
cv2.waitKey(0)

img1 = cv2.imread('Madhuri.JPG',1)
# print(img)
cv2.imshow('Window1', img1)
cv2.waitKey(0)

cv2.destroyAllWindows()
