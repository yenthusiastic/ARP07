"""
Simple shutdown button and status LED

insert as cron task:
crontab -e
@reboot sudo python /home/pi/ARP07/code/andy/shutdown.py &
"""

from gpiozero import Button
from gpiozero import LED
import os
from time import sleep

btn = Button(21)
led = LED(13)
led.on()

while True:
    if btn.is_pressed:
        print("btn pressed! waiting 3 sec")
        for i in range(3):
            led.off()
            sleep(0.5)
            led.on()
            sleep(0.5)
        if btn.is_pressed:
            os.system("sudo shutdown -h now")
    else:
        sleep(2)
