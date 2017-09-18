###################################################
# About
# Sepember 18 2017
# Step 2
# After 1000 datapoints were randomly sampled from the svanalyzer datasets, each entry must be selected from the union refalt vcf in order to run through svviz
# The following code finds matches between the union_170509_refalt vcf and the randomly sampled datapoints from svanalyzer datasets
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
Incorrect Match
'''

# Step 1: Load Data

colnames = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
df = pd.read_table('/Volumes/lesleydata/SVanalyzer_ML/Sept122017/Training_Data_SVanalyzer/Inaccruate_Call/svanalyzer_union_170509_refalt.2.2.2.clustered.uniquecalls_noheader_1000.txt', names=colnames)
df_vcf = pd.read_table('/Users/lmc2/union_170509_refalt.sort_formatted.txt', names=colnames)
print df.shape
print df_vcf.shape


print df.dtypes
print df_vcf.dtypes

df.B = df.B.astype(int)
print df.dtypes


'''
Step 2: Merge command on matching IDs

Note
-----
Some entries are listed more than once in the union vcf
'''

# Merge 2 dataframes based on matches in 1 column. Modify the names of the columns by adding a new suffix
df3 = pd.merge(df_vcf, df, on='B', how='inner', suffixes=('_vcf', '_svanalyzer'))
# print df3.head(3)
print df3.shape
# df3.to_csv('union_170509_refalt_match.csv', index=False)


'''
Step 3: Drop columns from svanalyzer

Note
----
After the merge step, columns from the merged dataframe are combined side by side. Drop the unneeded columns, svanalyzer columns
'''

df4 = df3[['A_vcf','B','C_vcf','D_vcf','E_vcf','F_vcf','G_vcf','H_vcf','I_vcf','J_vcf']]
df4.to_csv('/Volumes/lesleydata/SVanalyzer_ML/Sept122017/Training_Data_SVanalyzer/Inaccruate_Call/svviz/svviz_input_svanalyzer_union_170509_refalt.2.2.2.clustered.uniquecalls_1000.tsv', index=False, header=False, sep='\t')




'''
Homozygous Reference Match
'''

# Step 1: Load Data

colnames = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
df = pd.read_table('/Volumes/lesleydata/SVanalyzer_ML/Sept122017/Training_Data_SVanalyzer/Hom_Ref/HG002_v0.3.0b_homref_1000.txt', names=colnames)
df_vcf = pd.read_table('/Users/lmc2/union_170509_refalt.sort_formatted.txt', names=colnames)
print df.shape
print df_vcf.shape


print df.dtypes
print df_vcf.dtypes

df.B = df.B.astype(int)
print df.dtypes


'''
Step 2: Merge command on matching IDs

Note
-----
Some entries are listed more than once in the union vcf
'''

# Merge 2 dataframes based on matches in 1 column. Modify the names of the columns by adding a new suffix
df3 = pd.merge(df_vcf, df, on='B', how='inner', suffixes=('_vcf', '_svanalyzer'))
# print df3.head(3)
print df3.shape
# df3.to_csv('union_170509_refalt_match.csv', index=False)


'''
Step 3: Drop columns from svanalyzer

Note
----
After the merge step, columns from the merged dataframe are combined side by side. Drop the unneeded columns, svanalyzer columns
'''

df4 = df3[['A_vcf','B','C_vcf','D_vcf','E_vcf','F_vcf','G_vcf','H_vcf','I_vcf','J_vcf']]
df4.to_csv('/Volumes/lesleydata/SVanalyzer_ML/Sept122017/Training_Data_SVanalyzer/Hom_Ref/svviz/HG002_v0.3.0b_homref_1000.tsv', index=False, header=False, sep='\t')



'''
Exact Match
'''

# Step 1: Load Data

colnames = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
df = pd.read_table('/Volumes/lesleydata/SVanalyzer_ML/Sept122017/Training_Data_SVanalyzer/Exact_Match/HG002_multitechexact_v0.3.0b_1000.txt', names=colnames)
df_vcf = pd.read_table('/Users/lmc2/union_170509_refalt.sort_formatted.txt', names=colnames)
print df.shape
print df_vcf.shape


print df.dtypes
print df_vcf.dtypes

# df.B = df.B.astype(int)
# print df.dtypes


'''
Step 2: Merge command on matching IDs

Note
-----
Some entries are listed more than once in the union vcf
'''

# Merge 2 dataframes based on matches in 1 column. Modify the names of the columns by adding a new suffix
df3 = pd.merge(df_vcf, df, on='B', how='inner', suffixes=('_vcf', '_svanalyzer'))
# print df3.head(3)
print df3.shape
# df3.to_csv('union_170509_refalt_match.csv', index=False)


'''
Step 3: Drop columns from svanalyzer

Note
----
After the merge step, columns from the merged dataframe are combined side by side. Drop the unneeded columns, svanalyzer columns
'''

df4 = df3[['A_vcf','B','C_vcf','D_vcf','E_vcf','F_vcf','G_vcf','H_vcf','I_vcf','J_vcf']]
df4.to_csv('/Volumes/lesleydata/SVanalyzer_ML/Sept122017/Training_Data_SVanalyzer/Exact_Match/svviz/HG002_multitechexact_v0.3.0b_1000.tsv', index=False, header=False, sep='\t')





'''
Extra: Merge on multiple columns
'''
# Resourece: https://chrisalbon.com/python/pandas_join_merge_dataframe.html
# df4 = pd.merge(df_vcf, df, on=['D','E'], how='inner', suffixes=('_vcf', '_svanalyzer'))
# # print df4.head(3)
# print df4.shape
# # df3.to_csv('df3_ID_match.csv', index=False)

