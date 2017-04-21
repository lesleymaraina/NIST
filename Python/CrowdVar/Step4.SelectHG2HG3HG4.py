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
train_DEL = pd.read_csv('/Users/lmc2/Desktop/NIST/Projects/ML1-TrainingData/Code/PythonCode/Feb132017/ML.Training/svvizAllData.DEL.csv')
df_DEL = pd.DataFrame(train_DEL)

train_INS = pd.read_csv('/Users/lmc2/Desktop/NIST/Projects/ML1-TrainingData/Code/PythonCode/Feb132017/ML.Training/svvizAllData.INS.2.csv')
df_INS = pd.DataFrame(train_INS)


###################################################
# Code
###################################################

# Step 1: Select all rows that contain HG002, HG003, HG004 and store in a .csv
# Select HG002 Rows
df_DEL_HG002 = df_DEL[df_DEL['sample'].str.contains("HG002")]
print df_DEL_HG002.tail(8)
df_DEL_HG002.to_csv('/Users/lmc2/Desktop/NIST/Projects/ML1-TrainingData/Code/MLTrainingSets/March222017/DEL_HG002_1to1000.csv', index=False)


df_INS_HG002 = df_INS[df_INS['sample'].str.contains("HG002")]
print df_INS_HG002.tail(8)
df_INS_HG002.to_csv('/Users/lmc2/Desktop/NIST/Projects/ML1-TrainingData/Code/MLTrainingSets/March222017/INS_HG002_1to1000.csv', index=False)

# Select HG003 Rows
df_DEL_HG003 = df_DEL[df_DEL['sample'].str.contains("HG003")]
print df_DEL_HG003.tail(8)
df_DEL_HG003.to_csv('/Users/lmc2/Desktop/NIST/Projects/ML1-TrainingData/Code/MLTrainingSets/March222017/DEL_HG003_1to1000.csv', index=False)


df_INS_HG003 = df_INS[df_INS['sample'].str.contains("HG003")]
print df_INS_HG003.tail(8)
df_INS_HG003.to_csv('/Users/lmc2/Desktop/NIST/Projects/ML1-TrainingData/Code/MLTrainingSets/March222017/INS_HG003_1to1000.csv', index=False)

# Select HG004 Rows
df_DEL_HG004 = df_DEL[df_DEL['sample'].str.contains("HG004")]
print df_DEL_HG004.tail(8)
df_DEL_HG004.to_csv('/Users/lmc2/Desktop/NIST/Projects/ML1-TrainingData/Code/MLTrainingSets/March222017/DEL_HG004_1to1000.csv', index=False)


df_INS_HG004 = df_INS[df_INS['sample'].str.contains("HG004")]
print df_INS_HG004.tail(8)
df_INS_HG004.to_csv('/Users/lmc2/Desktop/NIST/Projects/ML1-TrainingData/Code/MLTrainingSets/March222017/INS_HG004_1to1000.csv', index=False)
