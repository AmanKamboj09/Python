import cv2
camera = cv2.VideoCapture(0) # open the webcam
while 1:
    ret,img = camera.read()
    print(ret)
    # Display an image in a window
    cv2.imshow('Live Video',img)
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('Grayscale Video', gray)
    if cv2.waitKey(1) == 27:
        break
camera.release()  # Close the Camera
cv2.destroyAllWindows()