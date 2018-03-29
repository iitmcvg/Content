import numpy as np
import cv2

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
cv2.line(img,(0,0),(511,511),(255,0,0),5)		#starting and ending coordinates

# cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)	#top left and bottom right coordinates

# cv2.circle(img,(447,63), 63, (0,0,255), -1)		#centre , radius , color ,thickness or filled

# cv2.ellipse(img,(256,256),(100,50),30,0,180,255,-1)		#centre, major and minor axis length, rotation angle, starting and ending angles clockwise,color,thickness or fill

# pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)	#coordinates
# pts = pts.reshape((-1,1,2))
# cv2.polylines(img,[pts],True,(0,255,255))			#True =>closed polygon

# font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)		#bottom left corner,type,size,color,line size,line type


cv2.namedWindow("Image",cv2.WINDOW_AUTOSIZE)

cv2.imshow("Image",img)

cv2.waitKey(0)			# press any key to exit

cv2.destroyAllWindows()