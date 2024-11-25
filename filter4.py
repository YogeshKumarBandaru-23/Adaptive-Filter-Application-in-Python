import cv2
import cvzone

def filter():
    video_capture = cv2.VideoCapture(0)
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    overlay = cv2.imread('joker2.png',cv2.IMREAD_UNCHANGED)
    #overlay2 = cv2.imread('joker_nose.png',cv2.IMREAD_UNCHANGED)
    
    while True:
        _,img = video_capture.read()
        gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray_img)
        for (x,y,w,h) in faces:
            overlay_resize = cv2.resize(overlay,(110+w,h+100))
            #overlay_resize2 = cv2.resize(overlay2,(w-60,h-60))
            #cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            frame = cvzone.overlayPNG(img,overlay_resize,[x-50,y-100])
            #frame = cvzone.overlayPNG(img,overlay_resize2,[x+30,y+40])
        cv2.imshow("Detected Face", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()
