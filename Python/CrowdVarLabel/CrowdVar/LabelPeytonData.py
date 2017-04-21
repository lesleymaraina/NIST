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

train = pd.read_csv('/Users/lmc2/Desktop/NIHFAES/FinalProject/Train/crowdVar.HiConf.csv')
df = pd.DataFrame(train)
print df.head()

'''
Select rows where:
CN0 >= 0.84
CN1 >= 0.84
CN2 >= 0.84
'''
mask_CN0 = (df['CN0_prob'] >= 0.84)
df_CN0 = df[mask_CN0]
df_CN0 ['label'] = 'CN0'
print df_CN0.head()

mask_CN1 = (df['CN1_prob'] >= 0.84)
df_CN1 = df[mask_CN1]
df_CN1 ['label'] = 'CN1'
print df_CN1.head()

mask_CN2 = (df['CN2_prob'] >= 0.84)
df_CN2 = df[mask_CN2]
df_CN2 ['label'] = 'CN2'
print df_CN2.head()

df_all = pd.concat([df_CN0,df_CN1,df_CN2], axis=0)
df_all = pd.DataFrame(df_all)
df_CN2.to_csv('/Users/lmc2/Desktop/NIHFAES/FinalProject/Train/CrowdVar_HiConf_labeled.csv')
print df_all.head()
print df_all.shape

'''
Store data in an external csv file 
'''
df_all.to_csv('/Users/lmc2/Desktop/NIHFAES/FinalProject/Train/CrowdVar_HiConf_labeled.csv', index=False)

