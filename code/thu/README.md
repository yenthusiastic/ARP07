### GUI app usage manual
#### Pre-installations
##### Python and pip
- Python version: 3.5
- pip3 package manager version 
##### Installing PyQt5
- Install dependencies
```bash
sudo apt-get update
sudo apt-get install qt5-default pyqt5-dev pyqt5-dev-tools
```
At this point, running `sudo apt-get install PyQt5` WILL NOT WORK on Raspbian. Instead have to build the library from source. On the Pi, download [sip-4.*.*.tar.gz](https://www.riverbankcomputing.com/software/sip/download) and [PyQt5_gpl-5.*.*.tar.gz](https://www.riverbankcomputing.com/software/pyqt/download5). Then run following command to extract them:
```bash
tar -xzvf sip-4.**.tar.gz
tar -xzvf PyQt5_gpl-5.**.tar.gz
```
- First have to build SIP:
```bash
cd sip-4.**
python3 configure.py
make
sudo make install
```
- When finished, repeat the same steps for building PyQt5
```bash
cd PyQt5_gpl-5.**
python3 configure.py --sip-module PyQt5.sip   #if this does not work, try 
python3 configure.py
make
sudo make install
```
##### Installing additional libraries:
- Adafruit Neopixel library `pip3 install rpi_ws281x adafruit-circuitpython-neopixel`
#### Running the app
- In current folder, run `sudo python3 main.py` to launch the GUI app.
#### GUI app manual
(image with details to be addded)
##### Touch buttons
- **Start/Stop** toggle button
  - Start: Run the data collection from hyperstrectral sensors
  - Stop: Stop the data collection from hyperstrectral sensors
- **Camera** toggle button
  - Enable/ disable camera preview
- **Settings** button
... (more to be added and explained)
##### Viewport
##### LED indicators
- Battery LED indicator
   - Red: battery critical
   - Yellow: battery weak
   - Green: battery good
- Data LED indicator
   - Blue: hyperspectral data transmission in progress
   - Off: no hyperspectral data transmission