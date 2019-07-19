#### Getting the Pi Zero to work with DS3231 RTC module from Adafruit 
- To enable I2C interface on the Pi (to communicate with the sensor), type in command
```bash
sudo raspi-config
```
- Go to **Inferfacing Options** -> **I2C** and enable it.
- Shut down the Pi 
```bash
sudo ahutdown -h now
```
- Connect DS3231 RTC module to Pi Zero according to following wiring schema

Raspberry Pi pin | RTC module pin 
---------|----------
 5V | Vin 
 GND | GND 
 SDA | SDA
 SCL | SCL

![](../media/raspberry-pi-pinout.png)

- Power RTC module with a CR1220 coin cell and turn on the Pi Zero again. 
- List the connected I2C devices on the Pi using the command
```bash 
sudo i2cdetect -y 1
```
- The output will show the I2C address of the DS3231 module. By default of the manufacturer (Adafruit), the I2C address of this module is 0x68, which corresponds with the terminal output:
![](../media/screenshot1.PNG)
- Run the example script `rtc.py`. Example output:
```
Program Started at: 2019-05-27 20:58:00
```
- However the timezone is not yet correct. To change the timezone, again go to the Raspberry Pi Config menu:
```bash
sudo raspi-config
```
- Go to **Localisation Options** -> **Change Timezone** and choose *Europe* -> *Berlin*. Reboot is not necessary.
- The system time of the Pi should be correct by the next reboot as long as the RTC is operating. To check this, reboot the Pi and use `date` command to check.
```bash
sudo reboot
date
```
