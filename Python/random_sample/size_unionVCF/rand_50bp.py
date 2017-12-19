###################################################
# About
# December 18 2017
# Sites randomly sampled base on size bins from union vcf [union_171212_refalt.sort.vcf.gz]
# Remove header via the command line : 
# grep -v "^#" /Users/lmc2/Downloads/union_171212_refalt.sort_1.txt > /Users/lmc2/Downloads/union_171212_refalt.sort_noheader.txt
# Time : ~28sec
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
Seperate VCF into INS and DEL
'''
# Load Data
colnames = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
df = pd.read_table('/Users/lmc2/Downloads/DEL_size_sample_5999.txt', names=colnames)
print (df.shape)
df.B = df.B.astype(int)
df['refLen'] = df['D'].astype('str')
df['refLen'] = df['refLen'].str.len()
df['altLen'] = df['E'].astype('str')
df['altLen'] = df['altLen'].str.len()
df['VariantType'] = np.where(df['refLen'] > df['altLen'], 'DEL', 'INS')
df['VariantType'].fillna('', inplace=True)
dfDel = df[df['VariantType'].str.contains("DEL")]
dfIns = df[df['VariantType'].str.contains("INS")]
dfDel.drop(['VariantType'], axis=1, inplace = True)
dfIns.drop(['VariantType'], axis=1, inplace = True)
# TIME [FYI] : 17.02sec

'''
Select Size Groups based on size bins
-------------
20-49
49-100
100-300
300-399
399-1000
1000-5999
6000+
'''

############
# Deletions
############

dfDel['Size'] = dfDel['altLen'] - dfDel['refLen']
dfDel['Size'] = dfDel['Size'].abs()

#Size Bins
bins = [0,19, 49,100,300,399,1000,5999,5000000]
dfDel['Size'] = dfDel['Size'].abs()
group_names_size = ['0-20', '20-49', '50-100', '100-300', '300-399', '400-1000', '1000-5999', '6000+']
dfDel['size_bin'] = pd.cut(dfDel['Size'], bins, labels=group_names_size)
dfDel['size_bin'] = dfDel.size_bin.astype(str)

df_20to50_del = dfDel[dfDel['size_bin'].str.contains('20-49')]
df_50to100_del = dfDel[dfDel['size_bin'].str.contains('50-100')]
df_100to300_del = dfDel[dfDel['size_bin'].str.contains('100-300')]
df_300to400_del = dfDel[dfDel['size_bin'].str.contains('300-399')]
df_400to1000_del = dfDel[dfDel['size_bin'].str.contains('400-1000')]
df_1000to6000_del = dfDel[dfDel['size_bin'].str.contains('1000-5999')]
df_6000_del = dfDel[dfDel['size_bin'].str.contains('6000+')]

# Randomly sample a total of 5999 DEL (857 per group)
df_20to50_del_ = pd.DataFrame(df_20to50_del)
df_50to100_del_ = pd.DataFrame(df_50to100_del)
df_100to300_del_ = pd.DataFrame(df_100to300_del)
df_300to400_del_ = pd.DataFrame(df_300to400_del)
df_400to1000_del_ = pd.DataFrame(df_400to1000_del)
df_1000to6000_del_ = pd.DataFrame(df_1000to6000_del)
df_6000_del_ = pd.DataFrame(df_6000_del)


all_ = pd.concat([df_50to100_del_, df_100to300_del_, df_300to400_del_, df_400to1000_del_, df_1000to6000_del_, df_6000_del_], axis=0)
all_ = all_.drop_duplicates()

all_.drop(['refLen'], axis=1, inplace = True)
all_.drop(['altLen'], axis=1, inplace = True)
all_.drop(['size_bin'], axis=1, inplace = True)
all_.drop(['Size'], axis=1, inplace = True)
print (all_.shape)
all_.to_csv('/Volumes/lesleydata/size_sample/Step1_ParseVCF/DEL_size_sample_5999_50bp+.vcf', sep='\t', header=None, index=False)

