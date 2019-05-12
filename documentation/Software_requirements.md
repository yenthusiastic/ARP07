### Requirements for GUI application
#### Functional requirements
##### The software shall be able to
- Retrieve and display spectral data on touchscreen
- Retrieve and display GPS data on touchscreen
- Retrieve and display date and time data on touchscreen
- Retrieve and display battery percentage on touchscreen
- Retrieve and display camera feed on touchscreen
- Mark and display FoV of optical fiber on current camera frame
- Detect and parse input configuration file from default USB device (volume labeled `INTERNAL`)
- Detect and handle user's input from touchscreen
- Store spectral data and corresponding captures on specified folder on default USB device
- Detect and copy all stored spectral data and corresponding captures from default USB device (`INTERNAL`) to secondary USB devices (volume labels starting with `DATA`, e.g. `DATA1`, `DATA_2`, `DATA_new`, etc.)

#### Non-functional requirements
- The software shall be compatible for the intended OS platform (headless, read-only Raspbian).
- The software shall be executed from a default USB device plugged into the Raspberry Pi.
- The software shall be able to stream its GUI to the touchscreen over HDMI interface.
- The application shall have a window size of 800x480 pixels.