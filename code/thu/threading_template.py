from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
import numpy as np


""" 
Template class to perform any task in the background to prevent freezing of GUI
and pass data from this class to another class that is calling the thread, i.e. GUI class
Methods and functions:
[ ] __init__(): initialize the thread
[ ] __del__(): destroy the thread
[ ] run(): the background task that runs in a while loop
... 
NOTE: items with [X] means completed, [+] newly added, [.] on-going, [ ] to-do 
"""

class myThread(QThread):
    # pyqtSignal to store the data of this thread that is to be emitted during running
    # replace np.array with the relevant data type
    mySignal = pyqtSignal(np.array, name='mySignal')
    def __init__(self):
        QThread.__init__(self)
        # add other initialzing functions or variables below
        

    def __del__(self):
        print("Stopping myThread")
        self.wait()

    def run(self):
        while True:
            # perform the background task to get data
            # ...

            data = np.array(1,2,3,4)  # example data

            # emit data from this thread to the GUI thread that is calling this thread
            self.mySignal.emit(data)

        # do something when the loop stops
        