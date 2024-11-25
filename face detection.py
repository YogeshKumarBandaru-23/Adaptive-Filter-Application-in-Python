import cv2
import cvzone
# def boundary(img, classifier,color):
#     gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#     features = classifier.detectMultiScale(gray_img,scaleFactor,minNeighbors)
#     coords = []
#     for (x,y,w,h) in features:
#         cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
#         coords = [x,y,w,h]
#     return coords,img
# def detect(img, faceCascade):
#     color = {"blue":(255,0,0),"red":(0,0,255),"green":(0,255,0)}
#     coords, img = boundary(img,faceCascade,1.1,10,color["blue"])
video_capture = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
overlay = cv2.imread('sunglass.png',cv2.IMREAD_UNCHANGED)
while True:
    _,img = video_capture.read()
    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray_img)
    # img = detect(img,faceCascade)
    for (x,y,w,h) in faces:
        # cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        overlay_resize = cv2.resize(overlay,(w,h))
        frame = cvzone.overlayPNG(img,overlay_resize,[x,y])
    cv2.imshow("Detected Face", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
