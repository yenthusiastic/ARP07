### Software research
#### Python libraries
##### For hardware components
- *Spectrometers:* 
- [DS3231 RTC module](https://github.com/switchdoclabs/RTC_SDL_DS3231), [Instruction](https://www.switchdoc.com/2014/08/raspberry-pi-python-library-ds3231/)
- Stream camera: [OpenCV](https://docs.opencv.org/4.1.0/d6/d00/tutorial_py_root.html), numpy
- [MTK3339 GPS module](https://github.com/PrzemoF/mtk3339)
- [Neopixel](https://learn.adafruit.com/neopixels-on-raspberry-pi/python-usage) (for power indication and data status)
##### For software components
- [PyYAML](https://pyyaml.org/wiki/PyYAML): Parse config file in YAML format: 
- OpenCV: Grab camera frame and draw FoV circle of optical fiber on image
- [Logger](https://docs.python.org/3/howto/logging.html)
- GUI for application: 
   -  Option 1 (simple): build native GUI application using [Tkinter](https://docs.python.org/3/library/tk.html) (included in Python installtion).
   -  Option 2 (medium): build native GUI app using [PyQt](https://pypi.org/project/PyQt5/) and Qt designer GUI app-builder
   -  Option 3 (medium): build web app and use [pywebview](https://github.com/r0x0r/pywebview) wrapper to display app in GUI window.

For now, option 2 is used as it comes with a GUI app builder (QtDesigner) that allows visualization of application layout.
- [Matchbox Keyboard](https://www.modmypi.com/blog/matchbox-keyboard-raspberry-pi-touchscreen-keyboard) (Virtual Keyboard for Raspberry Pi): Required for user to input custom parameters for spectrometer settings.

In order to change layout of the keyboard, follow instructions [here](https://www.raspberrypi.org/forums/viewtopic.php?t=122020).

#### Configuration file
- YAML file is a simple data structure based on key-value pairs that allows type parsing and hierarchical nodes, e.g: 
```yml
integer: 25
string: "25"
float: 25.0
boolean: Yes
parent_node:
 - child_node1
 - child_node2
 etc.
 ```
Sample configuration data to set parameters for the spectrometers in the project could be as follows:
```yml
itegration_time: 1234
acquisition_burst: 10
 ```
- Configurations to consider
   -  Directory of stored data
   - Directory of log files
   - Trigger button toggles
     - camera_enable: Yes/No
     - spectrometer1_enable: Yes/No
     - spectrometer2_enable: Yes/No
     - gps_enable: Yes/No
     - real_time_enable: Yes/No
   - Camera settings
   - Spectral settings
     - spectral_range
     - integration_time
     - acquisition_burst
