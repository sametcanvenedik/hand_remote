import cv2
import mediapipe as mp
import time


class handDetector():

    def __init__(self, mode= False, maxHands = 2, complexity = 1, detectionCon = 0.5, trackingCon = 0.5 ):
        self.mode = mode
        self.maxHands = maxHands
        self.complexity = complexity
        self.detectionCon = detectionCon
        self.trackingCon = trackingCon




        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.complexity, self.detectionCon, self.trackingCon)
        self.mpDraw= mp.solutions.drawing_utils


    def findHand(self, img, draw = True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.result = self.hands.process(imgRGB)
        #print(result.multi_hand_landmarks)
        
        if self.result.multi_hand_landmarks:
            for handLms in self.result.multi_hand_landmarks:
                if draw:    
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
               
               
        return img


    def findPosition(self, img, handNo =  0, draw = True):

        lmList = []
        if self.result.multi_hand_landmarks:
            myHand = self.result.multi_hand_landmarks[handNo]

            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                #print(id, cx, cy)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img,(cx, cy), 10, (255,0,255), cv2.FILLED)
        
        return lmList    

def main():

    cap = cv2.VideoCapture(0)

    pTime = 0
    cTime = 0
    detector = handDetector()

    while True:
        success, img = cap.read()
        
        if success:
            img = detector.findHand(img)
            lmlist = detector.findPosition(img)
            if len(lmlist) != 0:
                print(lmlist[4])


            cTime = time.time()
            fps = 1/(cTime-pTime)
            pTime = cTime
        
            cv2.putText(img, str(int(fps)), (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 1)
            cv2.imshow("mycam",img)
            cv2.waitKey(1)


if __name__ == "__main__":
    main()