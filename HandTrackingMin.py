import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
tim1=0


mpHands = mp.solutions.hands
hands = mpHands.Hands()

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(imgRGB)

    if success:
        tim2 = time.time()
        fps = str(int(1/(tim2-tim1)))
        tim1 = tim2
        cv2.putText(img, fps, (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 1)
        cv2.imshow("mycam",img)

    cv2.waitKey(1)
    