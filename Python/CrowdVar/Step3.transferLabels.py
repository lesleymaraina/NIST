############################################################
# About
# Date: March 31 2017

'''
Add High Confidence crowdVar Labels and percent certainty to original dataframe
'''
############################################################

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
all_data_DEL = pd.read_csv("/Users/lmc2/Desktop/NIHFAES/FinalProject/Train/CrowdVar.csv")

'''
Store Data in Dataframes
'''

mend_DEL = pd.read_csv('/Users/lmc2/Desktop/NIHFAES/FinalProject/Train/CrowdVar_HiConf_labeled.csv')
print mend_DEL.head(3)
# print all_data_DEL.head(3)


'''
Find matches between 2 dataframes and create a new column with corresponding label
'''

all_data_DEL['Label'] = -1

for j, i in enumerate(range(all_data_DEL.shape[0])):
	if j > 100000:
		break
	start_value = all_data_DEL.loc[i, 'start']
	start_indices = np.where(mend_DEL['start'] == start_value)[0].tolist()

	# end_value = all_data_DEL.loc[i, 'end']
	# end_indices = np.where(mend_DEL['end'] == end_value)[0].tolist()
	# index = set(start_indices) & set(end_indices)
	index = set(start_indices) 
	if len(index) == 0:
		continue
	# if len(index) > 1:
	# 	print("Unexpected hits found", i, index)
	# 	print(mend_DEL.loc[index, 'Counts'])
	# print(i, start_value, end_value, index)
	all_data_DEL.loc[i, 'Label'] = np.median(mend_DEL.loc[index, 'label2'])
	# print(all_data_DEL.loc[i])


all_data_DEL['CN0_prob'] = -1

for j, i in enumerate(range(all_data_DEL.shape[0])):
	if j > 100000:
		break
	start_value = all_data_DEL.loc[i, 'start']
	start_indices = np.where(mend_DEL['start'] == start_value)[0].tolist()
	# print(start_indices)
	# end_value = all_data_DEL.loc[i, 'end']
	# end_indices = np.where(mend_DEL['end'] == end_value)[0].tolist()
	# print(end_indices)
	index = set(start_indices) 
	if len(index) == 0:
		continue
	# if len(index) > 1:
	# 	print("Unexpected hits found", i, index)
	# 	print(mend_DEL.loc[index, 'Counts'])
	# print(i, start_value, end_value, index)
	all_data_DEL.loc[i, 'CN0_prob'] = np.median(mend_DEL.loc[index, 'CN0_prob'])


all_data_DEL['CN1_prob'] = -1

for j, i in enumerate(range(all_data_DEL.shape[0])):
	if j > 100000:
		break
	start_value = all_data_DEL.loc[i, 'start']
	start_indices = np.where(mend_DEL['start'] == start_value)[0].tolist()
	# print(start_indices)
	# end_value = all_data_DEL.loc[i, 'end']
	# end_indices = np.where(mend_DEL['end'] == end_value)[0].tolist()
	# print(end_indices)
	index = set(start_indices) 
	if len(index) == 0:
		continue
	# if len(index) > 1:
	# 	print("Unexpected hits found", i, index)
	# 	print(mend_DEL.loc[index, 'Counts'])
	# print(i, start_value, end_value, index)
	all_data_DEL.loc[i, 'CN1_prob'] = np.median(mend_DEL.loc[index, 'CN1_prob'])


all_data_DEL['CN2_prob'] = -1

for j, i in enumerate(range(all_data_DEL.shape[0])):
	if j > 100000:
		break
	start_value = all_data_DEL.loc[i, 'start']
	start_indices = np.where(mend_DEL['start'] == start_value)[0].tolist()
	# print(start_indices)
	# end_value = all_data_DEL.loc[i, 'end']
	# end_indices = np.where(mend_DEL['end'] == end_value)[0].tolist()
	# # print(end_indices)
	index = set(start_indices) 
	if len(index) == 0:
		continue
	# if len(index) > 1:
	# 	print("Unexpected hits found", i, index)
	# 	print(mend_DEL.loc[index, 'Counts'])
	# print(i, start_value, end_value, index)
	all_data_DEL.loc[i, 'CN2_prob'] = np.median(mend_DEL.loc[index, 'CN2_prob'])

print(all_data_DEL.head(10))
all_data_DEL.to_csv('/Users/lmc2/Desktop/NIHFAES/FinalProject/Train/CrowdVar.Train.csv', index=False)
all_data_DEL.to_csv('/Users/lmc2/Desktop/NIHFAES/FinalProject/Train/CrowdVar.Train.bed', index=False)



