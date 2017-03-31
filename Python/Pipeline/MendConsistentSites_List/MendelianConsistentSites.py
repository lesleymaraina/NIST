###################################################
# Imports 
# Selects all Mendelian Consistent Sites
###################################################
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

###################################################
# Data 
###################################################
train = pd.read_csv('/Users/lmc2/Desktop/NIST/Projects/ML1-TrainingData/Code/PythonCode/Feb132017/Mendelian/ROutput/10xMendelian.DEL.csv')
df = pd.DataFrame(train)

###################################################
# Code
###################################################

df2 = df[(df['HG002'] != -1) & (df['HG003'] != -1) & (df['HG004'] != -1)]
df4 = df[(df['HG002'] == -1) | (df['HG003'] == -1) | (df['HG004'] == -1)]
df5 = df[(df['HG002'] == 0) & (df['HG003'] == 0) & (df['HG004'] == 0)]
print df4.head(11)

mask = (((df2['HG002'] == 0) & (df2['HG003'] == 0) & (df2['HG004'] == 0)) | 
		(((df2['HG002'] == 1) | (df2['HG002'] == 0)) & (df2['HG003'] == 1) & (df2['HG004'] == 0)) |
	    ((df2['HG002'] == 1) & (df2['HG003'] == 2) & (df2['HG004'] == 0)) |
	    (((df2['HG002'] == 1) | (df2['HG002'] == 0)) & (df2['HG003'] == 0) & (df2['HG004'] == 1)) |
	    (((df2['HG002'] == 1) | (df2['HG002'] == 0) | (df2['HG002'] == 2)) & (df2['HG003'] == 1) & (df2['HG004'] == 1)) |
	    (((df2['HG002'] == 1) | (df2['HG002'] == 2)) & (df2['HG003'] == 1) & (df2['HG004'] == 2)) |
	    ((df2['HG002'] == 1) & (df2['HG003'] == 0) & (df2['HG004'] == 2)) |
	    (((df2['HG002'] == 1) | (df2['HG002'] == 2)) & (df2['HG003'] == 2) & (df2['HG004'] == 1)) |
	    ((df2['HG002'] == 2) & (df2['HG003'] == 2) & (df2['HG004'] == 2)))
df3 = df2[mask]
df3['technology'] = '10x'
# print df3.head()
# Total Sites
print df.shape
# MendInconsistent = df2-df5
print df2.shape
# All rows that contain -1
print df4.shape
# Mendelian consistent sites
print df3.shape
# Mendelian consistent sites, that have all zeros
print df5.shape
df3.to_csv('/Users/lmc2/Desktop/NIST/Projects/ML1-TrainingData/Code/PythonCode/Feb132017/Mendelian/MendOutput.Final/DEL/10x.Mend.DEL.csv')