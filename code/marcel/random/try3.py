import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import numpy as np

df = pd.read_csv("soc_curves.csv")
availableCs = np.unique([float(colName[-4:-1]) for colName in df.columns])

def get_lo(dischargeRate):
    """
    Get the lower available curve
    """
    return np.max(availableCs[availableCs < dischargeRate])

def get_hi(dischargeRate):
    """
    Get the higher available curve
    """
    return np.min(availableCs[availableCs > dischargeRate])

def get_soc(dischargeRate, voltage):
    """
    Takes in the momentary discharge rate (in C) and the voltage.
    Returns the current state of charge (SOC) in percents (0-100)
    Interpolates based on the 4 available curves (0.2C, 0.5C, 1C, 2C).
    Anything beyond the range gets clipped to 0.2C-2C.
    """
    dischargeRate = float(dischargeRate)
    dischargeRate = np.clip(dischargeRate,min(availableCs),max(availableCs))
    if dischargeRate in availableCs:
        voltage = np.clip(voltage, np.nanmin(df["v_{:.1f}C".format(dischargeRate)]), np.nanmax(df["v_{:.1f}C".format(dischargeRate)]))
        soc = 100 - np.interp(voltage,
                         df["v_{:.1f}C".format(dischargeRate)][np.logical_not(df["v_{:.1f}C".format(dischargeRate)].isnull())],
                         df["soc_{:.1f}C".format(dischargeRate)][np.logical_not(df["soc_{:.1f}C".format(dischargeRate)].isnull())])
        return np.clip(soc, 0, 100)
    else:
        rate_hi = get_hi(dischargeRate)
        v_hi = np.clip(voltage, np.nanmin(df["v_{:.1f}C".format(rate_hi)]), np.nanmax(df["v_{:.1f}C".format(rate_hi)]))
        soc_hi =  100 - np.interp(v_hi,
                            df["v_{:.1f}C".format(rate_hi)][np.logical_not(df["v_{:.1f}C".format(rate_hi)].isnull())],
                            df["soc_{:.1f}C".format(rate_hi)][np.logical_not(df["soc_{:.1f}C".format(rate_hi)].isnull())])
        
        rate_lo = get_lo(dischargeRate)
        v_lo = np.clip(voltage, np.nanmin(df["v_{:.1f}C".format(rate_lo)]), np.nanmax(df["v_{:.1f}C".format(rate_lo)]))
        soc_lo =  100 - np.interp(v_lo,
                            df["v_{:.1f}C".format(rate_lo)][np.logical_not(df["v_{:.1f}C".format(rate_lo)].isnull())],
                            df["soc_{:.1f}C".format(rate_lo)][np.logical_not(df["soc_{:.1f}C".format(rate_lo)].isnull())])
        #print(soc_lo, soc_hi, rate_lo, rate_hi)
        return np.clip(soc_lo + (dischargeRate - rate_lo) * (soc_hi - soc_lo) / (rate_hi - rate_lo), 0, 100)


# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)

# Create single-ended input on channel 0
chan0 = AnalogIn(ads, ADS.P0)
chan1 = AnalogIn(ads, ADS.P1)
chan2 = AnalogIn(ads, ADS.P2)

# Create differential input between channel 0 and 1
#chan = AnalogIn(ads, ADS.P0, ADS.P1)

#print("{:>5}\t{:>5}".format('raw', 'v'))

while True:
    vBat = chan0.voltage * 2
    iBatRaw = chan1.voltage * 2
    vHighHalf = chan2.voltage
    #vBat = np.random.randint(330,420)/100
    #vHighHalf = np.random.randint(490,510)/100 / 2
    #iBatRaw = vHighHalf + np.random.randint(20 ,100)/100
    iBat = (iBatRaw - vHighHalf) / 0.185
    cDis = iBat / 6.6
    print("{:>5.3f}\t{:>5.3f}\t{:>5.3f}\t{:>5.3f}\t{:>5.3f}\t{:>5.1f}".format(vBat, iBatRaw, vHighHalf, iBat, cDis, get_soc(cDis, vBat))
    time.sleep(5)
