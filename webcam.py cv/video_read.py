# pre-requisite for this:
# pip install opencv-contrib-python mediapipe
# run above code in terminal

import cv2
import numpy as np
path = r"D:\Chroma toons apps new update-- __ Background and new charecter आ गए --------(720P_HD).mp4"

cam = cv2.VideoCapture(path)  # webcam object
while cam.isOpened():
    status, frame = cam.read()  # read the video frame by 
    if not status:
         print(" Camera not available")
         break
    # display output
    cv2.imshow("webcam",frame)
    if cv2.waitKey(5) == ord('q'):
       cam.release()
       cv2.destroyAllWindows()
       break