import cv2
import datetime
import numpy as np

import ctypes


def hot_condition():
    ctypes.windll.user32.MessageBoxW(0, "It is a HOT CONDITION, Your attention required on this screen.", "ATTENTION", 0)
    # cv2.rectangle(image, (image.shape[0]/2 - 25 , image.shape[0]/2 - 25), (image.shape[0]/2 + 25 , image.shape[0]/2 + 25), [0, 0, 255], -1)
    # cv2.putText(image, "HOT CONDITION", (0, image.shape[0] - 25), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (0, 0, 0), 1)


face_cascade = cv2.CascadeClassifier('H:\\CroCon\\mains\\Assets\\haarcascade\\frontalface_default.xml')
cap = cv2.VideoCapture(0)
# image = cv2.imread('1.jpg')
now = datetime.datetime.now()
hour = now.hour
hot_count = 0
print('Time Now is ' + str(now.hour) + ':' + str(now.minute))
while True:
    ret, image = cap.read()
    if image.shape[1] > 1000:
        scale_percent = 60
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height)
        resize = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
        image = resize
    # image = cv2.imread('testnew.jpg')
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grayImage, 1.005)
    if len(faces) != 0:
        s = None
        if hour < 16:
            if faces.shape[0] >= 0:
                if faces.shape[0] < 10:
                    s = 'COLD'
                elif faces.shape[0] >= 10:
                    if faces.shape[0] < 30:
                        s = 'MILD'
                    elif faces.shape[0] >= 30:
                        s = 'HOT'
                        hot_count = hot_count + 1

        elif hour >= 20:
            if faces.shape[0] >= 0:
                if faces.shape[0] < 10:
                    s = 'COLD'
                elif faces.shape[0] >= 10:
                    if faces.shape[0] < 30:
                        s = 'MILD'
                    elif faces.shape[0] >= 30:
                        s = 'HOT'
                        hot_count = hot_count + 1
        else:
            if faces.shape[0] >= 0:
                if faces.shape[0] < 100:
                    s = 'COLD'
                elif faces.shape[0] >= 100:
                    if faces.shape[0] < 200:
                        s = 'MILD'
                    elif faces.shape[0] >= 200:
                        s = 'HOT'
                        hot_count = hot_count + 1
        print(s)
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 1)
        cv2.rectangle(image, (0, image.shape[0] - 25), (450, image.shape[0]), [255, 255, 255], -1)
        cv2.putText(image, "Number of faces detected: " + str(faces.shape[0]) + ", Condition : " + str(s),
                    (0, image.shape[0] - 10), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (0, 0, 0), 1)
    cv2.imshow('CroCon', image)
    if hot_count == 1:
        hot_condition()
    if cv2.waitKey(1) & 0xff == 27:
        break
image.release()
cv2.destroyAllWindows()
