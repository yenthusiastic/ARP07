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

