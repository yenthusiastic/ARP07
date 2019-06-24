from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
import os

""" 
Class to retrieve camera stream in the background to prevent freezing of GUI
[.] +Camera()
NOTE: items with [X] means completed, [+] newly added, [.] on-going, [ ] to-do 
"""

img_name = 'cap.png'
class Camera(QThread):
    # pyqtSignal to store the camera frame of this thread to be emitted during running
    frame_updated = pyqtSignal(int, name='frame_updated')
    def __init__(self):
        QThread.__init__(self)
        # initialize capturing
        

    def __del__(self):
        print("Stopping thread Camera")
        self.wait()

    def run(self):
        ret = os.system("python2 capture_frame.py")
        #print("exit code", ret)
        self.frame_updated.emit(ret)


            
            
            
            
       
        
    
        
    