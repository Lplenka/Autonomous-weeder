import cv2
import numpy as np
import time

import serial

ser = serial.Serial('/dev/ttyACM1', 9600, timeout=0.1)
flap = serial.Serial('/dev/ttyACM0', 9600, timeout=0.1)





#lower_green = np.array([40, 100, 50])
#upper_green = np.array([80, 255, 255])

cabbage_crossed = False
cabbage_present = False
prev_data = 0
khulja = []
khulja_pos = 0
bandhoja = []
bandhoja_pos = 0
error_a = 0
error_b = 0
time.sleep(3)
ser.write(bytes('a'.encode('ascii')))
data = ser.readline()[:-2]
print(data)
while(1):
    data = ser.readline()[:-2] 
    if data:
        print(data)


cv2.destroyAllWindows()
