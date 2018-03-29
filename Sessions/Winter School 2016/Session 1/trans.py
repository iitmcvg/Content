import cv2
import numpy as np

img = cv2.imread('ball_15cm.jpg')

cv2.namedWindow("Image",cv2.WINDOW_AUTOSIZE)

cv2.imshow("Image",img)

#cv2.INTER_AREA for shrinking and cv2.INTER_CUBIC (slow) & cv2.INTER_LINEAR for zooming

res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)	

cv2.namedWindow("Resized",cv2.WINDOW_AUTOSIZE)

cv2.imshow("Resized",res)

cv2.waitKey(0)

#OR

# height, width = img.shape[:2]
# res = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)

