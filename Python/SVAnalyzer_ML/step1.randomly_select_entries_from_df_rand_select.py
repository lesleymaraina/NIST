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
Inaccurate Calls
'''
# Load Data
df = pd.read_table('/Volumes/lesleydata/SVanalyzer_ML/Sept122017/Training_Data_SVanalyzer/Inaccruate_Call/svanalyzer_union_170509_refalt.2.2.2.clustered.uniquecalls_noheader.txt')

# Randomly select 1000 data points
row = random.sample(df.index, 1000)
df_new = df.ix[row]
df_new_2 = df_new.drop_duplicates()
# print df_new_2.shape

# Store randomly selected datapoints in a new vcf file
df_new_2.to_csv('/Volumes/lesleydata/SVanalyzer_ML/Sept122017/Training_Data_SVanalyzer/Inaccruate_Call/svanalyzer_union_170509_refalt.2.2.2.clustered.uniquecalls_noheader_1000.txt', sep='\t', header=None, index=False)
df_new_2.to_csv('/Volumes/lesleydata/SVanalyzer_ML/Sept122017/Training_Data_SVanalyzer/Inaccruate_Call/svanalyzer_union_170509_refalt.2.2.2.clustered.uniquecalls_noheader_1000.csv', header=None, index=False)


'''
Homozygous Reference Calls
'''
# Load Data
df = pd.read_table('/Volumes/lesleydata/SVanalyzer_ML/Sept122017/Training_Data_SVanalyzer/Hom_Ref/HG002_v0.3.0b_homref.txt')

# Randomly select 1000 data points
row = random.sample(df.index, 1000)
df_new = df.ix[row]
df_new_2 = df_new.drop_duplicates()
# print df_new_2.shape

# Store randomly selected datapoints in a new vcf file
df_new_2.to_csv('/Volumes/lesleydata/SVanalyzer_ML/Sept122017/Training_Data_SVanalyzer/Hom_Ref/HG002_v0.3.0b_homref_1000.txt', sep='\t', header=None, index=False)
df_new_2.to_csv('/Volumes/lesleydata/SVanalyzer_ML/Sept122017/Training_Data_SVanalyzer/Hom_Ref/HG002_v0.3.0b_homref_1000.csv', header=None, index=False)


'''
Exact Match Calls
'''
# Load Data
df = pd.read_table('/Volumes/lesleydata/SVanalyzer_ML/Sept122017/Training_Data_SVanalyzer/Exact_Match/HG002_multitechexact_v0.3.0b_noheader.txt')

# Randomly select 1000 data points
row = random.sample(df.index, 1000)
df_new = df.ix[row]
df_new_2 = df_new.drop_duplicates()
# print df_new_2.shape

# Store randomly selected datapoints in a new vcf file
df_new_2.to_csv('/Volumes/lesleydata/SVanalyzer_ML/Sept122017/Training_Data_SVanalyzer/Exact_Match/HG002_multitechexact_v0.3.0b_1000.txt', sep='\t', header=None, index=False)
df_new_2.to_csv('/Volumes/lesleydata/SVanalyzer_ML/Sept122017/Training_Data_SVanalyzer/Exact_Match/HG002_multitechexact_v0.3.0b_1000.csv', header=None, index=False)



