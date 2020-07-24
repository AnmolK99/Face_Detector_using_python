import cv2
cam=cv2.VideoCapture(0)
ccfr=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
while True:
    return_value,captured_frame=cam.read()

    grey_img=cv2.cvtColor(captured_frame,cv2.COLOR_BGR2GRAY)
    face=ccfr.detectMultiScale(grey_img,scaleFactor=1.05,minNeighbors=3)
    for x,y,w,h in face:
        captured_frame=cv2.rectangle(captured_frame,(x,y),(x+w,y+h),(255,255,255),1)
    cv2.imshow("Hello",captured_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
del(cam)

