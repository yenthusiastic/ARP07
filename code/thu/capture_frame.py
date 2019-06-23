from cv2 import VideoCapture, imwrite, destroyAllWindows
cap = VideoCapture(0)
for count in range(10):
	ret, frame = cap.read()
	print("Reading frame:", count)

#save the frame
imwrite('cap.png', frame)
# release the capture
cap.release()
destroyAllWindows()