# pre-requisite for this:
# pip install opencv-contrib-python mediapipe
# run above code in terminal

import cv2
import numpy as np

cam = cv2.VideoCapture(0)  # webcam object
while cam.isOpened():
    status, frame = cam.read()  # read the video frame by 
    if not status:
         print(" Camera not available")
         break
    # display output
    cv2.imshow("webcam",frame)
    if cv2.waitKey(1) == ord('s'):
       cam.release()
       cv2.destroyAllWindows()
       break