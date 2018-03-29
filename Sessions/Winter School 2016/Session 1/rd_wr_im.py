
import cv2

img=cv2.imread("ball_15cm.jpg",1)	#read image as color , greyscale =>0

cv2.namedWindow("Image",cv2.WINDOW_AUTOSIZE)

cv2.imshow("Image",img)



# hsv= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

# cv2.namedWindow("HSV",0)

# cv2.imshow("HSV",hsv)



# gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# cv2.namedWindow("gray",0)

# cv2.imshow("gray",gray)




# im_final=cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)

# cv2.namedWindow("BGR",0)

# cv2.imshow("BGR",im_final)


cv2.imwrite('test.png',img)



cv2.waitKey(0)			# press any key to exit

cv2.destroyAllWindows()
