############################################################
# Imports
############################################################
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pylab as p
import sklearn as sol

############################################################
# Load Data
############################################################
small_df = pd.read_table('/Users/lmc2/Desktop/NIHFAES/FinalProject/Train/Data/test/small_dataframe.csv')
large_df = pd.read_csv('/Users/lmc2/Desktop/NIHFAES/FinalProject/Train/Data/large_dataframe.csv')

print('Length of small dataframe is:', small_df.shape)
print('Length of large dataframe is:', large_df.shape)

'''
1. Find matches in small_df['chrom'] and large_df['chrom'] and small_df['start'] and large_df['start] 
2. Label each row with a match with '*' in a new column named 'extra'
'''

small_df['GT'] = -1

for j, i in enumerate(range(small_df.shape[0])):
	if j > 100:
		break
	start_value = small_df.loc[i, 'chrom']
	start_indices = np.where(large_df['chrom'] == start_value)[0].tolist()
	# print(start_indices)
	end_value = small_df.loc[i, 'start']
	end_indices = np.where(large_df['start'] == end_value)[0].tolist()
	# print(end_indices)
	index = set(start_indices) & set(end_indices)
	if len(index) == 0:
		continue
	# if len(index) > 1:
	# 	print("Unexpected hits found", i, index)
	# 	print(large_df.loc[index, 'Counts'])
	# print(i, start_value, end_value, index)
	small_df.loc[i, 'GT'] = np.median(large_df.loc[index, 'GT'])
	# print(small_df.loc[i])

# print(small_df.head(10))
small_df.to_csv('all3.csv', index=False)

'''
1. Find matches between 2 dataframes and create a new column with corresponding label
2. Create a new dataframe with the matching rows
'''

df2 = small_df[small_df['chrom'] == large_df['chrom']]
print df2.head()

mask = (small_df['start'] == large_df['start'])
df3 = all2[mask]
print df3.head()
