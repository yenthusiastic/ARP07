import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

import numpy as np

# Create the I2C bus
#i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
#ads = ADS.ADS1115(i2c)

# Create single-ended input on channel 0
#chan0 = AnalogIn(ads, ADS.P0)
#chan1 = AnalogIn(ads, ADS.P1)
#chan2 = AnalogIn(ads, ADS.P2)

# Create differential input between channel 0 and 1
#chan = AnalogIn(ads, ADS.P0, ADS.P1)

#print("{:>5}\t{:>5}".format('raw', 'v'))

while True:
    #vBat = chan0.voltage * 2
    #iBatRaw = chan1.voltage * 2
    #vHighHalf = chan2.voltage
    vBat = np.random.randint(330,420)/100
    vHighHalf = np.random.randint(490,510)/100 / 2
    iBatRaw = vHighHalf + np.random.randint(20 ,100)/100
    iBat = (iBatRaw - vHighHalf) / 0.185
    cDis = iBat / 6.6
    print("{:>5.3f}\t{:>5.3f}\t{:>5.3f}\t{:>5.3f}\t{:>5.3f}".format(vBat, iBatRaw, vHighHalf, iBat, cDis))
    time.sleep(5)
