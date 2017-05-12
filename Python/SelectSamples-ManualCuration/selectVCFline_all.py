###################################################
# About
# Date: May 11, 2017
# Description:
# Goal: Select sampled variant sites from union VCF
###################################################
# Imports 
###################################################
import pandas as pd
import random
import numpy as np

###################################################
# Data 
###################################################

# Load/Parse .txt file using pd.read_table()
colnames = ['chr', 'B', 'C', 'REF', 'ALT', 'F', 'G', 'H', 'I', 'J']
df = pd.read_table('/Users/lmc2/union_17505_refalt.sort.formattedforsvviz.AWK-SED.txt', names=colnames)
df2 = pd.read_csv('/Users/lmc2/sampled_calls.csv')
df2 = df2[['chr', 'REF', 'ALT']]

# print df.head()
# print df2.head()

df3 = pd.DataFrame()
df3 = pd.merge(df, df2, on=['chr','REF', 'ALT'])
print df3.head()

df3.to_csv('GIAB_sampled_calls.tsv', sep='\t', header=None, index=False)



