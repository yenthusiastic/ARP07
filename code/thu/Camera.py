from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
import os
import numpy as np
from PIL import Image


""" 
Class to retrieve camera stream in the background to prevent freezing of GUI
[.] +Camera()
NOTE: items with [X] means completed, [+] newly added, [.] on-going, [ ] to-do 
"""

img_name = 'cap.png'
class Camera(QThread):
    # pyqtSignal to store the camera frame of this thread to be emitted during running
    frame_updated = pyqtSignal(np.ndarray, name='frame_updated')
    def __init__(self):
        QThread.__init__(self)
        # initialize capturing
        

    def __del__(self):
        print("Stopping thread Camera")
        self.wait()

    def run(self):
        os.system("python2 capture_frame.py")
        try:
            img = Image.open(img_name)
            img.load()
            data = np.asarray(img)
             # emit camera frame to the GUI thread that is calling this thread
            self.frame_updated.emit(data)
        except:
            print("Unable to load ", img_name)
            self.frame_updated.emit(None)
            
       
        
    
        
    