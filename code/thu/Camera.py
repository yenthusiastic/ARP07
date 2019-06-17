from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
import sys
import time
import cv2
import numpy as np


""" 
Class to retrieve camera stream in the background to prevent freezing of GUI
[.] +Camera()
NOTE: items with [X] means completed, [+] newly added, [.] on-going, [ ] to-do 
"""

class Camera(QThread):
    # default camera port
    default_camera_port = "/dev/tty/USB0"
    # pyqtSignal to store the camera frame of this thread to be emitted during running
    frame_updated = pyqtSignal(np.ndarray, name='frame_updated')
    # flag to start or stop grabbing camera frames
    camera_on = True
    def __init__(self):
        QThread.__init__(self)
        # initialize capturing
        self.cap = cv2.VideoCapture(1)
        

    def __del__(self):
        print("Stopping thread Camera")
        
        self.wait()

    def run(self):
        while self.camera_on:
            # Capture frame
            ret, frame = self.cap.read()
            # convert color channels
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # emit camera frame to the GUI thread that is calling this thread
            self.frame_updated.emit(frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        # When camera off, release the capture
        self.cap.release()
        cv2.destroyAllWindows()