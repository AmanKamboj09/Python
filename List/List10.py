import cv2
list = ['Photos/1.jpg',
        'Photos/2.jpg',
        'Photos/3.jpg',
        'Photos/4.jpg',
        'Photos/5.jpg',
        'Photos/6.jpg',
        'Photos/7.jpg',
        'Photos/8.jpg']
for i in list:
    img = cv2.imread(i)
    cv2.imshow('Photos', img)
    cv2.waitKey(500)
cv2.destroyAllWindows()
