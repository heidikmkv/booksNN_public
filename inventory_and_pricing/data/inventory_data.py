# -*- coding: utf-8 -*-
"""
CDGD Python Dashboard

Created on Wed Aug 19 14:14:10 2020
@author: Lyra


Inputs: 
    * Inventory Health report from Amazon (contains age and stock level per SKU)
    * CDGD sourcing spreadsheet (contains seasonality classification and min/max prices)
    
Outputs: 
    * list of SKUs, min and max prices for each
    
"""
import pandas as pd
import numpy as np
import pyisbn #module for converting ISBN-13 to ISBN-10 and vice versa


invhealth = pd.read_csv('inventory_health_aug19.csv',engine='python')
FBAinv = pd.read_csv('FBA_inventory_aug19.csv',engine='python')
CDGD_inv = pd.read_csv('CDGD_inventory.csv')