from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
import sys
import time
import cv2
import numpy as np


""" 
Class to retrieve camera stream in the background to prevent freezing of GUI
[ ] +Camera()
NOTE: items with [X] means completed, [+] newly added, [.] on-going, [ ] to-do 
"""

class Camera(QThread):
    default_camera_port = "/dev/tty/USB0"
    frame_updated = pyqtSignal(str, name='frame_updated')
    camera_on = True
    def __init__(self):
        QThread.__init__(self)
        self.cap = cv2.VideoCapture(1)
        

    def __del__(self):
        print("Stopping thread Camera")
        
        self.wait()

    def run(self):
        while self.camera_on:
           # Capture frame-by-frame
            ret, frame = self.cap.read()

            # Display the resulting frame
            cv2.imshow('frame', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        # When camera off, release the capture
        self.cap.release()
        cv2.destroyAllWindows()