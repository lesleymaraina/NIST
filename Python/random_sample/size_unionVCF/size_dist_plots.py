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
import matplotlib.pyplot as plt
from matplotlib import pyplot
import seaborn as sns
###################################################
# Data 
###################################################

'''
Seperate VCF into INS and DEL
'''
# Load Data
colnames = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
df = pd.read_table('/Users/lmc2/Downloads/union_171212_refalt.sort_noheader.txt', names=colnames)
print (df.shape)
df['A'].replace('X', 23, inplace=True)
df['A'].replace('Y', 24, inplace=True)
df.A = df.A.astype(int)
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
dfDel = dfDel[dfDel['Size'] >= 50]
#Size Bins
dfDel['Size'] = dfDel['Size'].abs()
dfDel['log_size'] = np.log10(dfDel.Size)
sns.set_style("white")
# p = dfDel['A'].hist(alpha = 0.5, bins = 24, edgecolor='black', label='hom_var')
# p.grid(False)
# p.set_xlabel('Chromosome')
# p.set_ylabel('Frequency')
# p.set_title('Deletions_AllVariants_50bp+')
# plt.show(p)


############
# Insertions
############

dfIns['Size'] = dfIns['altLen'] - dfIns['refLen']
dfIns = dfIns[dfIns['Size'] >= 20]

#Size Bins
dfIns['Size'] = dfIns['Size'].abs()
dfIns['log_size'] = np.log10(dfIns.Size)
sns.set_style("white")
p = dfIns['A'].hist(alpha = 0.5, bins = 23, edgecolor='black', label='hom_var')
p.grid(False)
p.set_xlabel('Chromosome')
p.set_ylabel('Frequency')
p.set_title('Insertions_AllVariants_20bp+')
plt.show(p)


