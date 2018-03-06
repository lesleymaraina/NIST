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

# Load Data
colnames = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
df = pd.read_table('/Users/lmc2/Downloads/Sniffles_HG002_noheader.vcf', names=colnames)
df1 = df[df['E'].str.contains("INV")]
# Only Include Passing calls
df2 = df1[df1['G'].str.contains("PASS")]
# GT from Callers: Remove Hom Ref Calls
df3 = df2[~df2.J.str.contains("0/0")]
print (df3.head(3))
df3.to_csv('/Volumes/lesleydata/Inversions/March62018/inversions_Sniffles.vcf', sep='\t', header=None, index=False)

df = pd.read_table('/Users/lmc2/Downloads/MetaSV_HG002_noheader.vcf', names=colnames)
df1 = df[df['E'].str.contains("INV")]
# Only Include Passing calls
df2 = df1[df1['G'].str.contains("PASS")]
# GT from Callers: Remove Hom Ref Calls
df3 = df2[~df2.J.str.contains("0/0")]
print (df3.head(3))
df3.to_csv('/Volumes/lesleydata/Inversions/March62018/inversions_MetaSV.vcf', sep='\t', header=None, index=False)

'''
Add Headers Back When Finished
'''
