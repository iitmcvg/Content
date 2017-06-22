# Aim of this program is to use HOG to detect pedestrians (they are our objects now).
# We will be importing a pretrained SVM classifier for pedestrian detection. 
import cv2
import numpy as np

# Initialise HOG descriptor
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
# we call the setSVMDetector  to set the Support Vector Machine to be pre-trained pedestrian detector, 
#loaded via the cv2.HOGDescriptor_getDefaultPeopleDetector()  function.

image = cv2.imread("crop001623.png") #(Taken from INRIA Person Dataset)
image = cv2.resize(image, (400,400), interpolation = cv2.INTER_LINEAR)
# Resizing to reduce detection time and improve Detection accuracy
(rects, weights) = hog.detectMultiScale(image, winStride=(2, 2),padding=(8, 8), scale=1.05)
# The detectMultiScale  method constructs an image pyramid with scale=1.05
# and a sliding window step size of (4, 4)  pixels in both the x and y direction, respectively.

# Drawing the rectangle in our image
for (x, y, w, h) in rects:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

# Note: Non-Maxima Suppression is not done. Non maxima Suppression will improve the results quite well. This will
# suppress the bounding boxes which overlap more than certain given threshold. 

cv2.imshow("Image_with_people_detected", image)
cv2.waitKey()
cv2.destroyAllWindows()
