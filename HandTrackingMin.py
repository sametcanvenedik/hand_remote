import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
pTime = 0
cTime = 0


mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw= mp.solutions.drawing_utils


while True:
    success, img = cap.read()
    
    if success:
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = hands.process(imgRGB)

        #print(result.multi_hand_landmarks)
        
        if result.multi_hand_landmarks:
            for handLms in result.multi_hand_landmarks:
                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)



        cTime = time.time()
        fps = str(int(1/(cTime-pTime)))
        pTime = cTime
        
        cv2.putText(img, fps, (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 1)
        cv2.imshow("mycam",img)

    cv2.waitKey(1)
    