import cv2 
import numpy as np
import serial
from time import sleep
url = 'http://192.168.0.102:8080/video'

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(url)

class var:
       x = 0
       y = 0
def _map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
	
ser.write(f"{0},{0}".encode('utf-8'))
sleep(0.5)
ser.write(f"{180},{180}".encode('utf-8'))
sleep(0.5)
while True:
      ret,img = cap.read()
      img = cv2.resize(img,(500,400))
      img = cv2.rotate(img, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)
      gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
      faces = face_cascade.detectMultiScale(gray, 1.3, 5)
      for (x,y,w,h) in faces:
            mid_x = x+x+w
            mid_x = int(mid_x/2)
            mid_y = y+y+h
            mid_y = int(mid_y/2)
            if abs(mid_x-var.x) < 5:
                    #print("within range",var.x)
                    pass
            else:
                   print("not in range",var.x)
                   print(mid_x,mid_y)
                   angle_x = _map(mid_x,100,300,0,180)
                   angle_y = _map(mid_y,100,300,180,0)
                   if angle_x < 0:
                         angle_x = 0
                   elif angle_x > 180:
                         angle_x = 180
                   elif angle_y < 0:
                         angle_y = 0
                   elif angle_y > 180:
                         angle_y = 180
                   print("angles", angle_x, angle_y)
                   ser.write(f"{angle_x},{angle_y}".encode('utf-8'))
            var.x = mid_x
            var.y = mid_y
            cv2.rectangle(img, (x,y), (x+w, y+h), (128, 128, 0), 5)
            cv2.circle(img, (mid_x,mid_y), radius=5, color=(128, 128, 0), thickness=-1)
            if abs(mid_y-var.y) < 5:
                    #print("within range",var.x)
                    pass
            else:
                   print("not in range",var.x)
                   print(mid_x,mid_y)
                   angle_x = _map(mid_x,100,300,0,180)
                   angle_y = _map(mid_y,100,300,180,0)
                   if angle_x < 0:
                         angle_x = 0
                   elif angle_x > 180:
                         angle_x = 180
                   elif angle_y < 0:
                         angle_y = 0
                   elif angle_y > 180:
                         angle_y = 180
                   print("angles", angle_x, angle_y)
                   ser.write(f"{angle_x},{angle_y}".encode('utf-8'))
            var.x = mid_x
            var.y = mid_y
            cv2.rectangle(img, (x,y), (x+w, y+h), (128, 128, 0), 5)
            cv2.circle(img, (mid_x,mid_y), radius=5, color=(128, 128, 0), thickness=-1)
            
      cv2.imshow('Processing_Image',img)
      if cv2.waitKey(1) & 0xFF == ord('q'):
        ser.close()
        break


