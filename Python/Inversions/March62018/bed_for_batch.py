###################################################
# About
# March 6 2018
'''
Overall Goal
------------
Compare INV found using Sniffles(PB) and MetaSV(Ill) Callers to v0.5.0 calls

'''
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
Create BED File for BATCH Script
'''

# Sniffles
colnames = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
df = pd.read_table('/Volumes/lesleydata/Inversions/March62018/inversions_Sniffles.vcf', names=colnames)
df2 = pd.DataFrame()
df2 = df['H'].str.split(';',expand=True)
df2.columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M', 'N', 'O', 'P']
df3 = pd.DataFrame()
df3 = df2['D'].str.split('=',expand=True)
df4 = pd.DataFrame()
df4['chr'] = df['A']
df4['start'] = df['B'] - 300
df4['end'] = df3[1].astype(int)
df4['end'] = df4['end'] + 300
df4['name'] = 'Sniffles'
df4.to_csv('/Volumes/lesleydata/Inversions/March62018/Sniffles_BED_for_BATCH.bed', sep='\t', header=None, index=False)

# MetaSV
colnames = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
df = pd.read_table('/Volumes/lesleydata/Inversions/March62018/inversions_MetaSV.vcf', names=colnames)
df2 = pd.DataFrame()
df2 = df['H'].str.split(';',expand=True)
df3 = pd.DataFrame()
df3 = df2[0].str.split('=',expand=True)
df4 = pd.DataFrame()
df4['chr'] = df['A']
df4['start'] = df['B'] - 300
df4['end'] = df3[1].astype(int)
df4['end'] = df4['end'] + 300
df4['name'] = 'MetaSV'
print (df4.head(3))
df4.to_csv('/Volumes/lesleydata/Inversions/March62018/MetaSV_BED_for_BATCH.bed', sep='\t', header=None, index=False)