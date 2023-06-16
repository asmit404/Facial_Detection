#Importing Libraries
import cv2
from cv2 import FONT_HERSHEY_SIMPLEX

#Loading the cascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Face detection
cap = cv2.VideoCapture(0)
while True:
	ret, img = cap.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
		cv2.putText(img, "dumbass", (x,y), FONT_HERSHEY_SIMPLEX , 1.25 , (0,0,255))
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = img[y:y+h, x:x+w]

	# Display an image in a window
	cv2.imshow('img',img)

	# Wait for Esc key to stop
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break

# CLose the application
cap.release()
cv2.destroyAllWindows()
