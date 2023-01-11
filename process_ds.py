#!/usr/bin/env python
#-*- coding: utf-8 -*-

import xarray as xr
mpath = '/export/home/kbalem/Bureau/ISAS_SAMPLE'

def time_serie_on_point(lat,lon,var='TEMP',depth=1.0):

    #SHOULD DO SOME CHECKS ON VAR/LON/LAT/DEPTH VALUES HERE

    #
    
    ds = xr.open_mfdataset(mpath+'/*/*'+var+'.nc')
    dsi = ds[var].interp(depth=1.0,latitude=lat,longitude=lon,method='nearest')
    return dsi.values
    