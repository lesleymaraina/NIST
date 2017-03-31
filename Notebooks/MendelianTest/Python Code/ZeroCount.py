###################################################
# Imports 
###################################################
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

###################################################
# Data 
###################################################

train = pd.read_csv('MPMend.csv')
df = pd.DataFrame(train)


###################################################
# Code
###################################################
df2 = df[['HG002','HG003','HG004']]
result = df2.apply(pd.value_counts).fillna(0)
print result


df3 = df2[(df2['HG002'] == 0) & (df2['HG003'] == 0) & (df2['HG004'] == 0)]
result2 = df3.apply(pd.value_counts).fillna(0)
print result2