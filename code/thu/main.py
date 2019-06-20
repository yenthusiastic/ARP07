import sys
from GUI import start_GUI
import time

""" 
Class to handle I/O and hardware-related tasks
Functions to be included, as defined in Software Architecture:
[ ] -detect_USB_drive(): integer
[ ] -update_software(): integer
[X] -start_GUI(): integer
[ ] -update_configs(): integer
[ ] -store_data()
NOTE: items with [X] means completed, [+] newly added, [.] on-going, [ ] to-do 
"""


if __name__ == "__main__":
    start_GUI()  #call start_GUI() method from GUI.py to fire GUI
    #TODO: add remaining functions: detect_USB_drive(), update_software(), update_configs()
    while True:
        print("hello")
        time.sleep(1)