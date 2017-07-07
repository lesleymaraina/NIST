###################################################
# About
# Date: March 22, 2017
# Select specific rows that contain HG002, HG003, HG004 
# and store in an external .csv file to process for ML
# Will be used independetly for tSNE model
###################################################

###################################################
# Imports 
###################################################
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

###################################################
# Data 
###################################################
# Import machine learning training dataset
train_DEL = pd.read_csv('/Users/lmc2/NIST/Notebooks/CrowdVariant/Train/CrowdVar.Train.csv')
df_DEL = pd.DataFrame(train_DEL)



###################################################
# Code
###################################################

# Step 1: Select all rows that contain HG002, HG003, HG004 and store in a .csv
# Select HG002 Rows
df_DEL_HG002 = df_DEL[df_DEL['sample'].str.contains("HG002")]
print df_DEL_HG002.tail(8)
df_DEL_HG002.to_csv('/Users/lmc2/NIST/Notebooks/CrowdVariant/Train/Final_DF/CrowdVar.Train_HG002.csv', index=False)

# Select HG003 Rows
df_DEL_HG003 = df_DEL[df_DEL['sample'].str.contains("HG003")]
print df_DEL_HG003.tail(8)
df_DEL_HG003.to_csv('/Users/lmc2/NIST/Notebooks/CrowdVariant/Train/Final_DF/CrowdVar.Train_HG003.csv', index=False)

# Select HG004 Rows
df_DEL_HG004 = df_DEL[df_DEL['sample'].str.contains("HG004")]
print df_DEL_HG004.tail(8)
df_DEL_HG004.to_csv('/Users/lmc2/NIST/Notebooks/CrowdVariant/Train/Final_DF/CrowdVar.Train_HG004.csv', index=False)

