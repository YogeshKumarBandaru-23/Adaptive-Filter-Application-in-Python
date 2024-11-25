import cv2
import numpy as np
import cvzone

def cartoonify_stronger_frame(frame):
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   
    # Apply a median blur
    gray_blurred = cv2.medianBlur(gray, 7)
   
    # Detect edges using Laplacian filter for stronger edges
    edges = cv2.Laplacian(gray_blurred, cv2.CV_8U, ksize=5)
    edges = cv2.threshold(edges, 50, 255, cv2.THRESH_BINARY_INV)[1]
   
    # Use bilateral filter to reduce color palette
    color = cv2.bilateralFilter(frame, d=9, sigmaColor=200, sigmaSpace=200)
   
    # Reduce the number of colors using K-means clustering
    Z = color.reshape((-1, 3))
    Z = np.float32(Z)
    K = 9  # Number of clusters (i.e., colors)
    _, labels, centers = cv2.kmeans(Z, K, None,
                                    criteria=(cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0),
                                    attempts=10,
                                    flags=cv2.KMEANS_RANDOM_CENTERS)
    centers = np.uint8(centers)
    color_reduced = centers[labels.flatten()]
    color_reduced = color_reduced.reshape((frame.shape))
   
    # Combine edges with the color reduced image
    cartoon_strong = cv2.bitwise_and(color_reduced, color_reduced, mask=edges)
   
    return cartoon_strong

def cartoonify_video():
    # Capture video from webcam
    cap = cv2.VideoCapture(0)
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    overlay = cv2.imread('sunglass.png',cv2.IMREAD_UNCHANGED)

    while True:
        # Read each frame
        ret, frame = cap.read()
        gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray_img)
        if not ret:
            break

        # Apply cartoon effect to the frame
        cartoon_frame = cartoonify_stronger_frame(frame)
        for (x,y,w,h) in faces:
            # cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            overlay_resize = cv2.resize(overlay,(w,h))
            frame = cvzone.overlayPNG(cartoon_frame,overlay_resize,[x,y])

        # Display the resulting frame
        cv2.imshow('Cartoonify Stronger Effect', cartoon_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close windows
    cap.release()
    cv2.destroyAllWindows()

# Run the video cartoonification
