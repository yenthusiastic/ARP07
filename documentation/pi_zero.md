# Power
Supply: 5.20V, 2A 

CPU loading command: `seq -f '4/%g' 1 2 199999`


Components | mA Component | mA Total
---------|----------|----------
 Pi Zero W, GUI, idle, no RF | 90 mA | 90 mA
 100% CPU load | 70 mA | 160 mA
 \+ USB Hub | 15 mA | 175 mA
 \+ 2 USB-Drives | 125 mA | 300 mA
 \+ Monitor | 470 mA | 770 mA
 \+ Camera connected | 20 mA | 790 mA
 \+ Camera active | 110 mA | 900 mA



## Fresh Installation
**Files to change**
 - /boot/config.txt  `(hdmi, serial, I2C)`
 - /boot/ssh `(add his file so ssh is activated)`
 - /rootfs/etc/dhcpcd.conf  `(set static IP)`
 - /rootfs/etc/wpa_supplicant/wpa_supplicant.conf  `(WiFi network)`


## Mounting
### Make mount points
```bash
sudo mkdir /media/internal
sudo mkdir /media/data
sudo chown -R pi:pi /media/internal/
sudo chown -R pi:pi /media/data
```

Find volume to mount:
```bash
sudo mount -o uid=pi,gid=pi/dev/sda /media/internal/
```


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
