import cv2
from cv2 import RETR_TREE
import numpy as np

# Setting up both cameras for video capture
camL = cv2.VideoCapture(0)
camR = cv2.VideoCapture(1)

# Chweck to compare the frame sizes for each camera, not needed normally but a good check just in case
frame_width_L = int(camL.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height_L = int(camL.get(cv2.CAP_PROP_FRAME_HEIGHT))

frame_width_R = int(camR.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height_R = int(camR.get(cv2.CAP_PROP_FRAME_HEIGHT))

if frame_width_L != frame_width_R or frame_height_L != frame_height_R:
    #TODO: Allow users to user to use different camera sensors and set them to be equal resolutions
    raise cv2.error('Current implementation does not allow for cameras with different frame sizes, please change cameras to identical sensors') 

kernel = np.ones((7,7),np.uint8)