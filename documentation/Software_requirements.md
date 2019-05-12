### Requirements for GUI application
#### Functional requirements
##### The software shall be able to
- Retrieve spectral data upon press of trigger button
- Display spectral data on touchscreen
- Retrieve and display GPS data on touchscreen
- Retrieve and display date and time data on touchscreen
- Retrieve and display battery status on touchscreen
- Retrieve and display camera stream on touchscreen
- Mark and display FoV of optical fiber on current camera frame
- Detect and read configuration file from default USB device (volume labeled `INTERNAL`)
- Detect and handle user input from touchscreen
- Store spectral data and corresponding sensor data on default USB device (`INTERNAL`)
- Detect and copy all stored spectral data and corresponding sensor data from default USB device (`INTERNAL`) to secondary USB devices (volume labels starting with `DATA`, e.g. `DATA1`, `DATA_2`, `DATA_new`, etc.)
- Indicate data storage activity through hardware LEDs
- Stream GUI to the touchscreen over HDMI
- Generate logs on default USB device (`INTERNAL`)  
- Shut down the system gracefully upon corresponding touchscreen input or hardware input 

#### Non-functional requirements
- The software shall be compatible with the intended OS platform (headless, read-only Raspbian).
- The software shall be executed from a default USB device (volume labeled `INTERNAL`) plugged into the Raspberry Pi.
- The software on the default USB device (`INTERNAL`) should be updated through an external USB device (volume labels starting with `DATA`)
- The software shall have a window size of 800x480 pixels
- The software should have a user-friendly interface

