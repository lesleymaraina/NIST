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
train1 = pd.read_csv('10xMend.csv')
df = pd.DataFrame(train1)
train2 = pd.read_csv('300xMend.csv')
df2 = pd.DataFrame(train2)
train3 = pd.read_csv('250xMend.csv')
df3 = pd.DataFrame(train3)
train4 = pd.read_csv('MPMend.csv')
df4 = pd.DataFrame(train4)
train5 = pd.read_csv('PacBioMend.csv')
df5 = pd.DataFrame(train5)


###################################################
# Code
###################################################

new_df = pd.concat([df, df2, df3, df4, df5], axis=0)
new_df.to_csv('MendelianSummary.csv')