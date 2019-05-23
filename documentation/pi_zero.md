## Fresh Installation
**Files to change**
 - /boot/config.txt  `(hdmi, serial, I2C)`
 - /boot/ssh `(add his file so ssh is activated)`
 - /rootfs/etc/dhcpcd.conf  `(set static IP)`
 - /rootfs/etc/wpa_supplicant/wpa_supplicant.conf  `(WiFi network)`

### Notes
Install full desktop on headless raspian-lite image:

```sudo apt update && sudo apt install raspberrypi-ui-mods```


### Links
[Raspian Distros Download](https://www.raspberrypi.org/downloads/raspbian/)

[Installing Operation System Image](https://www.raspberrypi.org/documentation/installation/installing-images/README.md)

[Read-Only Raspberry Pi](https://learn.adafruit.com/read-only-raspberry-pi)

[Zero W power consumption](https://www.raspberrypi-spy.co.uk/2018/11/raspberry-pi-power-consumption-data/)

[Mounting disk by label](https://www.raspberrypi-spy.co.uk/2014/05/how-to-mount-a-usb-flash-disk-on-the-raspberry-pi/)

[Pi Zero Pinout](https://cdn.sparkfun.com/assets/learn_tutorials/6/7/6/PiZero_1.pdf)
