import cv2

img = cv2.imread('Madhuri1.jpg')

cv2.imshow('ORIGIONAL IMAGE', img)
cv2.waitKey(0)

IMG_HSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('HSV Image', IMG_HSV)
cv2.waitKey(0)
cv2.imshow('Hue Image', IMG_HSV[:,:,0])
cv2.waitKey(0)
cv2.imshow('Saturation Image', IMG_HSV[:,:,1])
cv2.waitKey(0)
cv2.imshow('Value Image', IMG_HSV[:,:,2])

cv2.waitKey(0)
cv2.destroyAllWindows()
