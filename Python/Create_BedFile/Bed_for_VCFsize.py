###################################################
# About
# February 13 2018
# IGV file
# Create a bed file which will note the size of the variant within the IGV session
###################################################

###################################################
# Imports 
###################################################
import pandas as pd
import random
import numpy as np

###################################################
# Data 
###################################################
'''
DEL
'''

# Load Data
colnames = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
df = pd.read_table('/Volumes/lesleydata/manual_Curation_app/images/IGV/bed2igvFiles/DEL_1000_manCur.sort_noheader.vcf', names=colnames)

# Create a new column that notes the type of variant INS or DEL
df.B = df.B.astype(int)
df['refLen'] = df['D'].astype('str')
df['refLen'] = df['refLen'].str.len()
df['altLen'] = df['E'].astype('str')
df['altLen'] = df['altLen'].str.len()
df['VariantType'] = np.where(df['refLen'] > df['altLen'], 'DEL', 'INS')
df['VariantType'].fillna('', inplace=True)

# Find the correct 'END' coordinate
'''
DEL
---
start - [altLen-refLen]
'''
df['size'] = df['altLen'] - df['refLen']
df['END'] = df['B'] - df['size']
df['size'] = df['size'].abs()

# Create a new dataframe to create the BED file
df2 = pd.DataFrame()
df2['chr'] = df['A']
df2['start'] = df['B']
df2['end'] = df['END']
df2['string1'] = df['VariantType']
df2['string2'] = df['size']
df2['string3'] = df['C']

df2['combined'] = df2['string1']+ ':' + df2['string2'].astype(str) + ':' + df2['string3']
df2.drop(['string1'], axis=1, inplace = True)
df2.drop(['string2'], axis=1, inplace = True)
df2.drop(['string3'], axis=1, inplace = True)

df2.to_csv('/Volumes/lesleydata/manual_Curation_app/images/IGV/bed2igvFiles/DEL_sizeBed.bed', sep='\t', header=None, index=False)

'''
INS
'''
# Load Data
colnames = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
df = pd.read_table('/Volumes/lesleydata/manual_Curation_app/images/IGV/bed2igvFiles/INS_1000_manCur.sort_noheader.vcf', names=colnames)

# Create a new column that notes the type of variant INS or DEL
df.B = df.B.astype(int)
df['refLen'] = df['D'].astype('str')
df['refLen'] = df['refLen'].str.len()
df['altLen'] = df['E'].astype('str')
df['altLen'] = df['altLen'].str.len()
df['VariantType'] = np.where(df['refLen'] > df['altLen'], 'DEL', 'INS')
df['VariantType'].fillna('', inplace=True)

# Find the correct 'END' coordinate
'''
INS
---
start + 1
'''
df['size'] = df['altLen'] - df['refLen']
df['END'] = df['B'] + 1

# Create a new dataframe to create the BED file
df2 = pd.DataFrame()
df2['chr'] = df['A']
df2['start'] = df['B']
df2['end'] = df['END']
df2['string1'] = df['VariantType']
df2['string2'] = df['size']
df2['string3'] = df['C']

df2['combined'] = df2['string1']+ ':' + df2['string2'].astype(str) + ':' + df2['string3']
df2.drop(['string1'], axis=1, inplace = True)
df2.drop(['string2'], axis=1, inplace = True)
df2.drop(['string3'], axis=1, inplace = True)
print(df2.head(1))

df2.to_csv('/Volumes/lesleydata/manual_Curation_app/images/IGV/bed2igvFiles/INS_sizeBed.bed', sep='\t', header=None, index=False)





