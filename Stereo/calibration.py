import cv2
from cv2 import RETR_TREE
import numpy as np
import threading
# # Setting up both cameras for video capture
# camL = cv2.VideoCapture(0)
# camR = cv2.VideoCapture(1)

# # Chweck to compare the frame sizes for each camera, not needed normally but a good check just in case
# frame_width_L = int(camL.get(cv2.CAP_PROP_FRAME_WIDTH))
# frame_height_L = int(camL.get(cv2.CAP_PROP_FRAME_HEIGHT))
# frame_width_R = int(camR.get(cv2.CAP_PROP_FRAME_WIDTH))
# frame_height_R = int(camR.get(cv2.CAP_PROP_FRAME_HEIGHT))

# if frame_width_L != frame_width_R or frame_height_L != frame_height_R:
#     #TODO: Allow users to user to use different camera sensors and set them to be equal resolutions
#     raise cv2.error('Current implementation does not allow for cameras with different frame sizes, please change cameras to identical sensors') 

# kernel = np.ones((7,7),np.uint8)

class camThread(threading.Thread):
    def __init__(self, previewName, camID):
        threading.Thread.__init__(self)
        self.previewName = previewName
        self.camID = camID
    def run(self):
        print("Starting " + self.previewName)
        camPreview(self.previewName, self.camID)

def camPreview(previewName, camID):
    cv2.namedWindow(previewName)
    cam = cv2.VideoCapture(camID)
    if cam.isOpened():  # try to get the first frame
        rval, frame = cam.read()
    else:
        rval = False

    while rval:
        cv2.imshow(previewName, frame)
        rval, frame = cam.read()
        key = cv2.waitKey(20)
        if key == 27:  # exit on ESC
            break
    cv2.destroyWindow(previewName)

# Create two threads as follows
thread1 = camThread("Camera 1", 0)
thread2 = camThread("Camera 2", 1)
thread1.start()
thread2.start()