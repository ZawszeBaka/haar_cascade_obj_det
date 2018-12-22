import cv2
import numpy as np

cap = cv2.VideoCapture('video/out.avi')
# out = cv2.VideoWriter('video/for_train.avi', cv2.VideoWriter_fourcc('M','J','P','G'), 10, (int(cap.get(3)), int(cap.get(4))))
out = cv2.VideoWriter('test/for_test.avi', cv2.VideoWriter_fourcc('M','J','P','G'), 10, (int(cap.get(3)), int(cap.get(4))))
# cap.set(2, 0.74)

saved_frames = [[0,300],[700,800],[2200, 2290]]
#saved_frames = [[1100, 1300]]

if cap.isOpened() == False:
    print(' [ERROR] opening video stream or file failed ')

iframe = 0
while cap.isOpened():
    ret, frame = cap.read()

    if ret == True:
        iframe += 1

        for _range in saved_frames:
            if iframe <= _range[1] and iframe >= _range[0]:
                out.write(frame)
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                gray = cv2.resize(gray, (50,50))
                cv2.imwrite('neg_video/'+ str(iframe) + '.jpg', gray)
                # break

        # cv2.imshow('frame', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()

cv2.destroyAllWindows()
