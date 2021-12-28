import cv2 
import numpy as np
import serial
from time import sleep

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
sleep(2)
ser.write(f"{0},{0}".encode('utf-8'))
sleep(2)
ser.write(f"{180},{180}".encode('utf-8'))
