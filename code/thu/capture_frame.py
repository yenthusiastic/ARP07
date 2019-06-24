from cv2 import VideoCapture, imwrite, destroyAllWindows
cap = VideoCapture(0)
for count in range(10):
	ret, frame = cap.read()
	if ret:
		print("Reading frame:", count)
	else:
		print("Failed to read camera frame")
		exit(-1)

#save the frame
imwrite('cap.png', frame)
# release the capture
cap.release()
destroyAllWindows()
