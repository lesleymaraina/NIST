#######################################################################
# About
# -----
# 
# Date: June 30, 2017
#
# Notes
# -----
# Change GIAB Data GT labels so that they match CrowdVar GT Labels

#######################################################################

#######################################################################
# Import
#######################################################################

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#######################################################################
# Load Data
#######################################################################

train = pd.read_csv('/Users/lmc2/NIST/Notebooks/CrowdVariant/svviz.Annotate.DEL.HG002_data.csv')
df = pd.DataFrame(train)


'''
Select rows where:
CN0 >= 0.84
CN1 >= 0.84
CN2 >= 0.84
'''
mask_CN0 = (train['GTcons'] == 0)
df_CN0 = train[mask_CN0]
df_CN0['GIAB_Crowd'] = '2'
# print df_CN0.head()

mask_CN2 = (train['GTcons'] == 2)
df_CN2 = train[mask_CN2]
df_CN2['GIAB_Crowd'] = '0'

mask_CN1 = (train['GTcons'] == 1)
df_CN1 = train[mask_CN1]
df_CN1['GIAB_Crowd'] = '1'


df_all = pd.concat([df_CN0,df_CN2,mask_CN1], axis=0)
df_all = pd.DataFrame(df_all)
# print df_all.head()
# print df_all.shape

'''
Store data in an external csv file 
'''
df_all.to_csv('/Users/lmc2/NIST/Notebooks/CrowdVariant/svviz.Annotate.DEL.HG002_2.csv', index=False)

