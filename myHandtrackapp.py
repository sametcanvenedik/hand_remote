import cv2
from matplotlib.pyplot import draw
import mediapipe as mp
import time
import HandTrackingModule as hm


cap = cv2.VideoCapture(0)

pTime = 0
cTime = 0
detector = hm.handDetector()

while True:
    success, img = cap.read()
    
    if success:
        img = detector.findHand(img)
        lmlist = detector.findPosition(img, draw = False)
        if len(lmlist) != 0:
            print(lmlist[4])


        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
    
        cv2.putText(img, str(int(fps)), (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 1)
        cv2.imshow("mycam",img)
        cv2.waitKey(1)