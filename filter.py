#!/usr/bin/python

import face_recognition
import cv2
import numpy as np

#Filter file
unique = cv2.imread('christmas_unique_filter.png', 1)
cap = cv2.VideoCapture(0)

def put_unique(uni,fc,x,y,w,h):
    face_width = w
    face_height = h

    uni = cv2.resize(uni,(int(face_width*1),int(face_height*1.9)))
    for i in range(int(face_height*1.9)):
        for j in range(int(face_width*1)):
            for k in range(3):
                if uni[i][j][k]<235:
                    fc[y+i-int(0.375*h)-1][x+j-int(0.25*w)][k] = uni[i][j][k]
    return fc

while True:
    ret, frame = cap.read()
    #Convert
    rgb_frame = frame[:, :, ::-1]
    #rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    face_loc = face_recognition.face_locations(rgb_frame)

    for (x, y, w, h) in face_loc:
        #Draw box around face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        frame = put_unique(unique,frame,x,y,w,h)

    cv2.imshow('Unique Salonga Filter', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
