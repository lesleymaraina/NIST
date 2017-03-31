###################################################
# Imports 
###################################################
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

###################################################
# Data 
###################################################
# Will select all insertions from this dataframe
train = pd.read_csv('/Users/lmc2/Desktop/NIST/Projects/ML1-TrainingData/Code/PythonCode/Feb132017/ROutputForPython/INS/Output/10x.INS.csv')
df = pd.DataFrame(train)
# print df.head(5)

df['start'] = df['start'] + 1

print df.head(3)

df.to_csv('/Users/lmc2/Desktop/NIST/Projects/ML1-TrainingData/Code/PythonCode/Feb132017/ROutputForPython/INS/Output/10x.2.INS.csv', index=False)