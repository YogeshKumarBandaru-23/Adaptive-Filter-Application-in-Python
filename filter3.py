import cv2
import cvzone

def filter():
    video_capture = cv2.VideoCapture(0)
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    overlay = cv2.imread('ash.png',cv2.IMREAD_UNCHANGED)
    while True:
        _,img = video_capture.read()
        gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray_img)
        for (x,y,w,h) in faces:
            overlay_resize = cv2.resize(overlay,(w+20,h))
            # cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            frame = cvzone.overlayPNG(img,overlay_resize,[x,y-int(h/2)])
        cv2.imshow("Detected Face", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()