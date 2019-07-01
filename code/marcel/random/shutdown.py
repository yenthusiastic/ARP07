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
        sleep(3)
        if btn.is_pressed:
            os.system("sudo shutdown -h now")
    else:
        sleep(1)
