import cv2

framewidth=640
frameheight=360

cap=cv2.VideoCapture("resources/sample.mp4")

while True:
    success,img=cap.read()
    cv2.imshow("video",img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
