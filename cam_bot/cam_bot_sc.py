import cv2 
import numpy as np
import serial
url = 'http://192.168.0.100:8080/video'

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(url)

while True:
      ret,img = cap.read()
      img = cv2.resize(img,(500,400))
      img = cv2.rotate(img, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)
      gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
      faces = face_cascade.detectMultiScale(gray, 1.3, 5)
      for (x,y,w,h) in faces:
            print(x,y,w,h)
            cv2.rectangle(img, (x,y), (x+w, y+h), (29, 0, 100), 2)
            #img = cv2.circle(img, (center_x,center_y), radius=0, color=(0, 0, 255), thickness=-1)
            ser.write(f"{x},{y},{w},{h}".encode('utf-8'))
      cv2.imshow('Processing_Image',img)
      if cv2.waitKey(1) & 0xFF == ord('q'):
        ser.close()
        break
