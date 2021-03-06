## Instructions for cloning OS image and run GUI app
Most current image available on [Google Drive](https://drive.google.com/drive/u/0/folders/1s-zRTGhcLGHEpJTI93D9O8YIeo6DgwfC).

### Image version log
- Build 13.06.19: Raspian + PyQt5 + dependencies for RTC, GPS, Neopixel. 
- Build 09.07.19: b13.06.19 + pyqtgraph + dependencies for ADC, Seabreeze for Spectrometer
- Build 12.07.19: b09.07.19 + openCV compiled, tested working with python3


### Flash OS Image on SD-Card
#### On Linux
[raspberrypi.org - Installing operating system images](https://www.raspberrypi.org/documentation/installation/installing-images/README.md)

`sudo dd bs=4M if=pizero_ARP_gui_compiled_20190613_shrunk.img of=/dev/sde status=progress conv=fsync`
#### On Windows:
Install [Rufus](https://rufus.ie/) or use the portable executable to flash the image. (tested working)

###  Re-Expand Root Partition on Raspberry Pi 

`sudo raspi-config --expand-rootfs`

Whenf inished, **reboot Raspberry Pi**.

### Check that the partition is expanded
```bash
df -h
```
The root partition should now take the whole SD card volume
![fs screenshot](../media/fs_screencap.png)

### Test GUI application
Use the [arp07.sh](../misc/arp07.sh) script to get the latest release tag and execute the application. Or to do this manually:
- Get the zipped Source Code version 180719 from https://github.com/yenthusiastic/ARP07/tags
- Extract the zip file and run the GUI
```bash
cd ARP07-b180719
sudo python3 main.py        #sudo is required to control GPIO pins
```
GUI of version 180719 looks like follows
![GUI screenshot](../media/GUI_180719_1.PNG)

