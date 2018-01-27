###################################################
# Date : Jan 19 2018
'''
Description
-----------
Change size of deletions listed on Google sheet
https://docs.google.com/spreadsheets/d/1UkmYk_ghAVIWJX6oLN5RaieS2PZTGoXRKVyY36uEzxo/edit#gid=0
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
Step 1
'''

colnames = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
df = pd.read_table('/Volumes/lesleydata/size_sample/Step1_ParseVCF_svvizScripts/VCF_files/DEL/DEL_1000_manCur.vcf', names=colnames)
df_vcf = pd.read_csv('/Volumes/lesleydata/size_sample/Step1_ParseVCF_svvizScripts/VCF_files/DEL/del_subSample.csv')
print (df.head(1))


'''
Step 2: Merge command on matching IDs
Note
-----
Some entries are listed more than once in the union vcf
'''

# Merge 2 dataframes based on matches in 1 column. Modify the names of the columns by adding a new suffix
df3 = pd.merge(df, df_vcf, on=['C'], how='inner', suffixes=('_vcf', '_svanalyzer'))
df3.rename(columns={'A_vcf': 'chrom'}, inplace=True)
df3.rename(columns={'B': 'start'}, inplace=True)

print (df3.head(3))
print (df3.shape)
df3.to_csv('/Volumes/lesleydata/manual_Curation_app/images/change_DEL_subsampSize.csv', index=False)
