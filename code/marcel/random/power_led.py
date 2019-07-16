from gpiozero import LED
from time import sleep

led = LED(19)
led.on()
while True:
    sleep(30)
