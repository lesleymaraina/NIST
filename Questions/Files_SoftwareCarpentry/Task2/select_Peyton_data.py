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

# Load/Parse .txt file using pd.read_table()
colnames = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
union_VCF = pd.read_table('/Users/lmc2/Desktop/NIST/Projects/ML1-TrainingData/Code/VCF_files/Feb142017.Output/union_refalt.sort.Jan31.3.txt', names=colnames)
crowdVar = pd.read_csv('/Users/lmc2/Desktop/NIHFAES/FinalProject/Train/Data2.csv')

union_df = pd.DataFrame(union_VCF)

'''
1. Find matches between 2 dataframes and create a new column with corresponding label
2. Label each row with a match with '2' in a new column named 'extra'
'''

union_VCF['extra'] = -1

for j, i in enumerate(range(union_VCF.shape[0])):
	if j > 100:
		break
	start_value = union_VCF.loc[i, 'A']
	start_indices = np.where(crowdVar['chrom'] == start_value)[0].tolist()
	# print(start_indices)
	end_value = union_VCF.loc[i, 'B']
	end_indices = np.where(crowdVar['start'] == end_value)[0].tolist()
	# print(end_indices)
	index = set(start_indices) & set(end_indices)
	if len(index) == 0:
		continue
	# if len(index) > 1:
	# 	print("Unexpected hits found", i, index)
	# 	print(crowdVar.loc[index, 'Counts'])
	# print(i, start_value, end_value, index)
	union_VCF.loc[i, 'extra'] = np.median(crowdVar.loc[index, 'extra'])
	# print(union_VCF.loc[i])

# print(union_VCF.head(10))
union_VCF.to_csv('all3.csv', index=False)

'''
1. Find matches between 2 dataframes and create a new column with corresponding label
2. Create a new dataframe with the matching rows
'''

all2 = pd.read_csv('/Users/lmc2/all2.csv')
print all2.head()
df2 = all2[all2['B'] == all2['start']]
print df2.head()

mask = (all2['B'] == all2['start'])
df3 = all2[mask]
print df3.head()
