import cv2
import numpy as np

def nothing(x):
    pass

# Create a black image, a window
img = cv2.imread("ball_15cm.jpg",0)

cv2.namedWindow('image',cv2.WINDOW_AUTOSIZE)

# create trackbars for color change
cv2.createTrackbar('Threshold','image',0,255,nothing)


while(1):
   
   # get current positions of the trackbar
   
    thresh_val = cv2.getTrackbarPos('Threshold','image')

    ret,thresh = cv2.threshold(img,thresh_val,255,cv2.THRESH_BINARY)

    cv2.imshow('image',thresh)


    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    

cv2.destroyAllWindows()

