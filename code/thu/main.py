import sys
from GUI import start_GUI
import time
import seabreeze
seabreeze.use("cseabreeze")
import seabreeze.spectrometers as sb
import seabreeze.backends
lib = seabreeze.backends.get_backend()

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

def init_spectrometers():
    print("Looking for spectrometer devices...")
    devices = sb.list_devices()
    print(devices)
    
    lib.device_close(devices[0])
    lib.device_close(devices[1])
    #print(sb.Spectrometer(devices[0]))

    try:
        return sb.Spectrometer(devices[0]), sb.Spectrometer(devices[1])
    except:
        print("Can't connect to two Spectrometers.")

if __name__ == "__main__":
    #init_spectrometers()
    start_GUI()  #call start_GUI() method from GUI.py to fire GUI
    #TODO: add remaining functions: detect_USB_drive(), update_software(), update_configs()
