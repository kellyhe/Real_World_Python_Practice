"""Detect faces in video capture using Haar Cascade."""
import cv2 as cv
import sysconfig


# Path to OpenCV's Haar Cascades
path = sysconfig.get_paths()['purelib'] + '/cv2/data/'
face_cascade = cv.CascadeClassifier(path + 'haarcascade_frontalface_alt.xml')

cap = cv.VideoCapture(0)

while True:
    # Capture frame-by-frame
    _, frame = cap.read()
    face_rects = face_cascade.detectMultiScale(frame, scaleFactor=1.2,
                                               minNeighbors=4)    

    for (x, y, w, h) in face_rects:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
    # Display the resulting frame
    cv.imshow('frame', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture
cap.release()
cv.destroyAllWindows()
