import sys
from GUI import start_GUI


""" 
Class to handle I/O and hardware-related tasks
Functions to be included, as defined in Software Architecture:
[ ] -detect_USB_drive(): integer
[ ] -update_software(): integer
[X] -start_GUI(): integer
[ ] -update_configs(): integer
NOTE: items with [X] means completed, [+] newly added, [.] on-going, [ ] to-do 
"""


if __name__ == "__main__":
    start_GUI()  #call start_GUI() method from GUI.py to fire GUI
    #TODO: add remaining functions: detect_USB_drive(), update_software(), update_configs()