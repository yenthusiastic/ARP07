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
 - /boot/ssh `(add this file so ssh is activated)`
 - /rootfs/etc/dhcpcd.conf  `(set static IP)`
 - /rootfs/etc/wpa_supplicant/wpa_supplicant.conf  `(setup WiFi network)`

## Image
### Current Image
Download: [pizero_ARP_gui_compiled_20190613_shrunk.img](https://drive.google.com/drive/folders/1s-zRTGhcLGHEpJTI93D9O8YIeo6DgwfC) 3.6 GB

## Flash Image on SD-Card
[raspberrypi.org - Installing operating system images](https://www.raspberrypi.org/documentation/installation/installing-images/README.md)

`sudo dd bs=4M if=pizero_ARP_gui_compiled_20190613_shrunk.img of=/dev/sde status=progress conv=fsync`

###  Re-Expand Root Partition on Raspberry Pi 

`sudo raspi-config --expand-rootfs`

### Make Image of SD-Card
[The PiHut - Backing up and Restoring your Raspberry Pi's SD Card](https://thepihut.com/blogs/raspberry-pi-tutorials/17789160-backing-up-and-restoring-your-raspberry-pis-sd-card)
`sudo dd if=/dev/sde of=pizero_ARP_gui_compiled_20190613_full.img status=progress conv=fsync`


### Shrink Image
[Adafruit: Shrinking Images](https://learn.adafruit.com/resizing-raspberry-pi-boot-partition/bonus-shrinking-images)

As ubuntu uses a loot of loop devices at */dev/loopXX*, I modified the script to use */dev/loop90* which should not be in use.
To make sure, enter `ls /dev/loop90` into the terminal, the directory should not exist!
If it exist, change all **loop90** in the script to another number, not listed in `ls /dev/loop*`.

Call the script with `sudo shrink_img.sh <name.img>`.

shrink_img.sh:
```bash
#!/bin/env bash
 
IMG="$1"
 
if [[ -e $IMG ]]; then
  P_START=$( fdisk -lu $IMG | grep Linux | awk '{print $2}' ) # Start of 2nd partition in 512 byte sectors
  P_SIZE=$(( $( fdisk -lu $IMG | grep Linux | awk '{print $3}' ) * 1024 )) # Partition size in bytes
  losetup /dev/loop90 $IMG -o $(($P_START * 512)) --sizelimit $P_SIZE
  fsck -f /dev/loop90
  resize2fs -M /dev/loop90 # Make the filesystem as small as possible
  fsck -f /dev/loop90
  P_NEWSIZE=$( dumpe2fs /dev/loop90 2>/dev/null | grep '^Block count:' | awk '{print $3}' ) # In 4k blocks
  P_NEWEND=$(( $P_START + ($P_NEWSIZE * 8) + 1 )) # in 512 byte sectors
  losetup -d /dev/loop90
  echo -e "p\nd\n2\nn\np\n2\n$P_START\n$P_NEWEND\np\nw\n" | fdisk $IMG
  I_SIZE=$((($P_NEWEND + 1) * 512)) # New image size in bytes
  truncate -s $I_SIZE $IMG
else
  echo "Usage: $0 filename"
fi
```


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
