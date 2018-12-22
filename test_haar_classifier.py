
import cv2
import numpy as np

cap = cv2.VideoCapture('test/for_test.avi')

sign_cascade = cv2.CascadeClassifier('data/cascade.xml')

if cap.isOpened() == False:
    print(' [ERROR] opening video stream or file failed ')

while cap.isOpened():
    ret, frame = cap.read()

    if ret == True:

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # img, scale factor, min neighbors
        signs = sign_cascade.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in signs:
            cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 3)

        cv2.imshow('img', frame)
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()
