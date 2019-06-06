import sys
from GUI_handler import start_GUI

# All functions of main program to be included, as defined in Software Architecture:
# [ ] -detect_USB_drive(): integer
# [ ] -update_software(): integer
# [X] -start_GUI(): integer
# [ ] -update_configs(): integer
# NOTE: items with [X] means checked, else means to-do
if __name__ == "__main__":
    start_GUI()  #call start_GUI() method from GUI_handler.py to fire GUI
    #TODO: add remaining functions: detect_USB_drive(), update_software(), update_configs()