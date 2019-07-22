### Requirements for GUI application
#### Functional requirements
##### The software shall be able to
- Retrieve spectral data in real-time
- Display spectral data in real-time
- Retrieve and display real-time GPS data from GPS module
- Retrieve and display date and time from RTC module
- Retrieve and display real-time battery status
- Retrieve and display real-time data transmission status
- Retrieve and display camera stream upon request (touch button)
- Detect and handle user input from touchscreen
- Store spectral data with meta-data (geo-info, date time) on default USB device (`INTERNAL`) upon a press of the trigger button
- Store camera capture with meta-data (date time) on default USB device (`INTERNAL`) upon a press of the trigger button
- Detect and copy all stored data from default USB device (`INTERNAL`) to secondary USB devices (volumes labelled with other names than `INTERNAL`)
- Indicate data storage activity and battery status through hardware LEDs
- Shut down the system gracefully upon corresponding touchscreen input or hardware input

**TODOs:**
- *Mark and display FoV of optical fiber on current camera frame*
- *Detect and read configuration file from default USB device (volume labeled `INTERNAL`)*
- *Generate logs on default USB device (`INTERNAL`)*


#### Non-functional requirements
- The software shall be excuted on a Raspberry Pi 3 Model B
- The software shall be compatible with the intended OS platform (Raspbian Stretch).
- The software shall have a window size of 600x450 pixels
- The GUI shalle be streamed to the touchscreen over HDMI
- The software should have a user-friendly interface

**TODOs:**
- *The software shall be executed from a default USB device (volume labeled `INTERNAL`) plugged into the Raspberry Pi.*
- *The software on the default USB device (`INTERNAL`) should be updated through an external USB device (volume labbels with other names than `INTERNAL`)*

