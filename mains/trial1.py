import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('H:\\CroCon\\mains\\Assets\\haarcascade\\frontalface_default.xml')
eyes_cascade = cv2.CascadeClassifier('H:\\CroCon\\mains\\Assets\\haarcascade\\eyes.xml')
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.5, 5)
    print(type(faces))
    if len(faces):
        print("No faces found")
    else:
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]
        cv2.rectangle(frame, ((0, frame.shape[0] - 25)), (270, frame.shape[0]), (255, 255, 255), -1)
        cv2.putText(frame, "Number of faces detected: " + str(faces.shape[0]), (0, frame.shape[0] - 10), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (0, 0, 0), 1)
        # eyes = eyes_cascade.detectMultiScale(roi_gray)
        # for (ex,ey,ew,eh) in eyes:
        #   cv2.rectangle(roi_color, (ex, ey), ((ex+ew),(ey+eh)), (0,255,0), 2)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        cap.release()
        cv2.destroyAllWindows()
