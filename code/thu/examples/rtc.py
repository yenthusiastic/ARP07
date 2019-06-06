# coding: utf-8
# imports

import sys
import time
import datetime

import SDL_DS3231

# Main Program

print('Program Started at: '+ time.strftime('%Y-%m-%d %H:%M:%S'))

filename = time.strftime('%Y-%m-%d%H:%M:%SRTCTest') + '.txt'
starttime = datetime.datetime.utcnow()

ds3231 = SDL_DS3231.SDL_DS3231(1, 0x68)
ds3231.write_now()

# Main Loop – reads and prints values of RTC every 10 seconds
while True:

    currenttime = datetime.datetime.utcnow()

    deltatime = currenttime - starttime

    print('Raspberry Pi=\t' + time.strftime('%Y-%m-%d %H:%M:%S'))

    print('DS3231=\t\t%s' % ds3231.read_datetime())

    time.sleep(10.0)
