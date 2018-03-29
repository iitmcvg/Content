
import cv2

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))			#frames per second and framesize


while(cap.isOpened()):
	ret, frame = cap.read()
	if ret==True:
		frame = cv2.flip(frame,0)

        # Our operations on the frame come here
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	    # Display the resulting frame
		cv2.imshow('frame',gray)

        # write the flipped frame
		# out.write(frame)

		cv2.imshow('frame',gray)
	    
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	
	else:
		break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
