import picamera2
import cv2
import numpy as np
from time import sleep
file = "/home/Root/Documents/CV-Presentation/tuning_files/pisp/imx219_noir.json"
tuning_file = picamera2.Picamera2.load_tuning_file(file)
picamL = picamera2.Picamera2(1, tuning=tuning_file)
picamR = picamera2.Picamera2(0, tuning=tuning_file)

picamL.start()
picamR.start()

while(True):
    #This is bread and butter time bbi

    frameL = picamL.capture_array()
    frameR = picamR.capture_array()

    cv2.imshow('Left Camera', frameL)
    cv2.imshow('Right Camera',frameR)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
