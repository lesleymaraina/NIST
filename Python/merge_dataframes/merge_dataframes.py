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
Step 1
'''

colnames = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
df = pd.read_table('/Volumes/lesleydata/size_sample/Step1_ParseVCF_svvizScripts/VCF_files/INS/INS_1000_manCur.vcf', names=colnames)
df_vcf = pd.read_csv('/Volumes/lesleydata/size_sample/Step4_ML/dataframes/Step1_CombinedDFs/ins_HG002.csv')
print (df.head(1))
# print (df_vcf.shape)

df_vcf.rename(columns={'chrom': 'A'}, inplace=True)
df_vcf.rename(columns={'start': 'B'}, inplace=True)

# print df.dtypes
# print df_vcf.dtypes

# df.B = df.B.astype(int)
# print df.dtypes


'''
Step 2: Merge command on matching IDs
Note
-----
Some entries are listed more than once in the union vcf
'''

# Merge 2 dataframes based on matches in 1 column. Modify the names of the columns by adding a new suffix
df3 = pd.merge(df_vcf, df, on=['B'], how='inner', suffixes=('_vcf', '_svanalyzer'))
df3.rename(columns={'A_vcf': 'chrom'}, inplace=True)
df3.rename(columns={'B': 'start'}, inplace=True)

print (df3.head(3))
print (df3.shape)
df3.to_csv('/Volumes/lesleydata/manual_Curation_app/images/sampleSelect_INS.csv', index=False)
