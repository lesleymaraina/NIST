#######################################################################
# About
# -----
# 
# Date: March 29, 2017
#
# Notes
# -----
# Add a new column to Peyton's CrowdVar Data that lists high confidence 
# varaint call label in 1 column
# CN0	Variant where values are >= 0.84
# CN1	Het     where values are >= 0.84
# CN2	Reference where values are >= 0.84
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

train = pd.read_csv('/Users/lmc2/NIST/Notebooks/CrowdVariant/X9.csv')
df = pd.DataFrame(train)


'''
Select rows where:
CN0 >= 0.84
CN1 >= 0.84
CN2 >= 0.84
'''
mask_CN0 = (df['CrowdVar_0'] >= 0.6)
df_CN0 = df[mask_CN0]
df_CN0 ['model_label'] = '0'
# print df_CN0.head()

mask_CN_0_5 = (df['CrowdVar_0'] == 0.5)
df_CN_0_5 = df[mask_CN_0_5]
df_CN_0_5 ['model_label'] = '0.5'

mask_CN1 = (df['CrowdVar_1'] >= 0.6)
df_CN1 = df[mask_CN1]
df_CN1 ['model_label'] = '1'
# print df_CN1.head()

mask_CN0_5_2 = (df['CrowdVar_1'] == 0.5)
df_CN0_5_2 = df[mask_CN0_5_2]
df_CN0_5_2 ['model_label'] = '0.5'

mask_CN2 = (df['CrowdVar_2'] >= 0.6)
df_CN2 = df[mask_CN2]
df_CN2 ['model_label'] = '2'
# print df_CN2.head()

df_all = pd.concat([df_CN0,df_CN1,df_CN2,df_CN_0_5,df_CN0_5_2], axis=0)
df_all = pd.DataFrame(df_all)
# print df_all.head()
# print df_all.shape

'''
Store data in an external csv file 
'''
df_all.to_csv('/Users/lmc2/NIST/Notebooks/CrowdVariant/CrowdVar_Model_labeled.csv', index=False)

