# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import geopandas as gpd

shp = gpd.read_file('NHDSnapshot/Hydrography/NHDFlowline.shp')

dbf = gpd.read_file('NHDPlusAttributes/PlusFlowlineVAA.dbf')
dbf = dbf[['ComID','StreamOrde']]
a = shp.merge(dbf, left_on='COMID', right_on='ComID', how='left')

a.geometry = a.geometry.centroid
a.to_crs({'init': 'epsg:4326'}, inplace=True) # WGS 84 -- the default
#a.plot()
a[['COMID', 
   'REACHCODE', 
   'FLOWDIR', 
   'WBAREACOMI', 
   'FTYPE', 
   'StreamOrde', 
   'geometry']].to_file('~/Documents/catitat/delivery/data/flow_03N_centroid.shp')
