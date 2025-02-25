import cv2
from cv2 import RETR_TREE
import numpy as np

cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
kernel = np.ones((7,7),np.uint8)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsvInvert = cv2.bitwise_not(hsv)

    # define range of pink color in an inverted HSV

    lower_red = np.array([85, 80, 80])
    upper_red = np.array([145, 200, 200])

    # Threshold the HSV image to get only pink colors
    mask = cv2.inRange(hsvInvert, lower_red, upper_red)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    #finding and sorting the countours of the area
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    if contours:
        (xMin, yMin, boxWidth, boxHeight) = cv2.boundingRect(contours[0])

        cv2.rectangle(frame, (xMin - 15, yMin - 15), (xMin + boxWidth + 15, yMin + boxHeight + 15), (0, 0, 0), 4)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    cv2.imshow('hsv', hsvInvert)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()