import cv2 
import numpy as np
url = 'http://192.168.0.102:8080/video'
#face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_eye_tree_eyeglasses.xml')
face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(url)
class var:
       x = 0
       y = 0
def _map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
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
             var.x = mid_x
             var.y = mid_y
             cv2.rectangle(img, (x,y), (x+w, y+h), (128, 128, 0), 5)
             cv2.rectangle(img, (x-10,y-10), (x+w+10, y+h+10), (128, 128, 0), 2)
             cv2.circle(img, (int(mid_x),int(mid_y)), radius=5, color=(128, 128, 0), thickness=-1)
             angle_x = _map(mid_x,100,300,0,180)
             angle_y = _map(mid_y,100,300,180,0)
             print("angles", angle_x, angle_y)
             #print(mid_x,mid_y)
      cv2.imshow('VR',img)
      if cv2.waitKey(1) & 0xFF == ord('q'):
        break