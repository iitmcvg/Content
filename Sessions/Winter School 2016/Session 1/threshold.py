import cv2
import numpy as np


img = cv2.imread('ball_15cm.jpg',0)
ret,thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
# ret,thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
# ret,thresh = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
# ret,thresh = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
# ret,thresh = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

cv2.namedWindow("Image",cv2.WINDOW_AUTOSIZE)

cv2.imshow("Image",thresh)

cv2.waitKey(0)