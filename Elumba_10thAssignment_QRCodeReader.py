import numpy as np
import cv2
from pyzbar.pyzbar import decode
import time
import datetime

def info_from_input(frameF):
     for code in decode(frameF):
        file_maker = open("DataInput.txt", "w")
        file_maker.write(f"{code.data.decode('utf-8')}\n")
        date_info = datetime.datetime.now()
        file_maker.write(date_info.strftime("%y-%m-%d %H:%M:%S"))
        file_maker.close()
        time.sleep(2)

capture_device = cv2.VideoCapture(0)
capture_device.set(3, 360)
capture_device.set(4, 240)
camera = True

while camera == True:
    success, frame = capture_device.read()
    info_from_input(frame)
    cv2.imshow('ScanningDeviceFaceHere', frame)
    cv2.waitKey(1)