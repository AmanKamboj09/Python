import cv2

img = cv2.imread('s2/2.jpg',1)
print(img.shape)
resized = cv2.resize(img,(500,400))
Half = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
print()
# print(img)
cv2.imshow('Brij1', img)
cv2.imshow('Resized',resized)
cv2.imshow('Half',Half)
cv2.waitKey(0)
cv2.destroyAllWindows()
