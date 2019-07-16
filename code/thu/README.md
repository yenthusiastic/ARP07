### GUI app usage manual
#### Tag history
- b130619: GUI works with RTC, Neopixel, matchbox keyboard (requires Raspbian image 130619)
- b170619: b130619 + GUI works with Camera (requires building openCV - Raspbian image to be created)
   - Update 240619: removed due to failure to compile OpenCV on Raspberry Pi
- b240619: b130619 + GUI works with trigger button + single capture of camera frame when triggered + settings dialog
- b010719: GUI works with spectrometer sensors & power electronics

#### Running the app
Make sure all libraries are installed for the GUI to function properly.
```bash
sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel
sudo pip3 install adafruit-circuitpython-ads1x15
sudo apt install python3-pyqtgraph
# install seabreeze (TO DO)
```
- In current folder, run `sudo python3 main.py` to launch the GUI app.
#### GUI app manual
##### Main Spectrometer Window
![GUI_screencap](../../media/GUI_010719.PNG)
##### Camera capture window
![GUI_screencap](../../media/GUI_screencap240619_1.PNG)
###### Labels
- **Batt** label: display battery level (in %)
   - Battery LED indicator
      - Red: battery below 30%
      - Yellow: battery between 30% and 70%
      - Green: battery above 70%
- **Data** label: display status of data transmission to USB drives
   - Data LED indicator
      - Blue: hyperspectral data transmission in progress
      - Off: no hyperspectral data transmission
- **Date time** label
   - Show current date time (obtained from RTC)
- **Location** label
   - Show current location (latitude & longitude, obtain from GPS)
###### Touch buttons
- **Capture** button
  - Capture a frame from camera and display it in GUI. Takes 10s on average to complete
- **Calibrate** button
   - Calibrate the spectrometers
- **Start/Stop** toggle button
  - Start: Run the data collection from hyperstrectral sensors
  - Stop: Stop the data collection from hyperstrectral sensors
- **Settings** button
  - Show a pop-up window to edit configurations for spectrometers

##### Settings pop-up window
![Settings_screencap](../../media/GUI_screencap240619_2.PNG)
###### Sliders
- **Spectral range** slider
   - Min: 190 nm
   - Max: 1650 nm
   - Step size: 100 nm
- **Integration time** slider
   - Min: 1 ms
   - Max: 1000 ms
   - Step size: 100 ms
- **Acquisition burst** slider
   - Min: 1 
   - Max: 100 
   - Step size: 10
- **OK** button
   - confirm the new parameter values
