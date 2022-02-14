from time import time
import cv2
from cv2 import cuda
import time
cap = cv2.VideoCapture(0)
pTime = 0
cTime = 0

while True:

    suc, img = cap.read()

    if suc:
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1)
        img = cv2.bilateralFilter(img, 30, 100, 100)
        cv2.imshow("my Cam", img)
        cv2.waitKey(1)
