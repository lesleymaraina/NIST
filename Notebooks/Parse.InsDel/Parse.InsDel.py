###################################################
# Imports 
###################################################
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

###################################################
# Data 
###################################################
# Will select all insertions from this dataframe
train = pd.read_csv('/Users/lmc2/Desktop/NIST/Projects/ML1-TrainingData/Code/RCode/Feb42017/MPtest.csv')
df = pd.DataFrame(train)
# print df.head(5)

# Will select all deletions from this dataframe
trainDel = pd.read_csv('/Users/lmc2/Desktop/NIST/Projects/ML1-TrainingData/Code/RCode/Feb42017/MPtest.csv')
df2 = pd.DataFrame(trainDel)
# print df2.head(5)

###################################################
# Code
###################################################

# Step 1: Insertions

df = df[df['variant'].str.contains("Insertion")]
print df.tail(8)
SV_count3 = pd.crosstab(index=df['type'], columns="count")
print SV_count3

def length1(len):
	len_1 = len.split(';')[1]
	# len_2 = len_1[2].split('=')[0]
	return len_1


def length2(len):
	len_1 = len.split('=')[1]
	# len_2 = len_1[2].split('=')[0]
	return len_1

results = pd.DataFrame()
results['length'] = df['variant'].apply(length1)
results['lengthNum'] = results['length'].apply(length2)
# print results.head()

df['length'] = results['lengthNum'].astype(int)
# print df.head(5)
# print df.dtypes

diff = df['end'] - df['start']
df['Size'] = df['length'] - diff
# print inser


def InsDel(name):
	if name > 0:
		return 'Insertion'
	elif name < 0:
		return 'Deletion'


df['SVtype'] = df['Size'].apply(InsDel)
# print df.head(5)


SV_count = pd.crosstab(index=df['SVtype'], columns="count")
print SV_count


# Step 2: Deletions
df2 = df2[df2['variant'].str.contains("Deletion")]
print df2.tail(18)
SV_count = pd.crosstab(index=df2['type'], columns="count")
print SV_count

diff2 =  df2['start'] - df2['end']
df2['Size'] =  diff2
# print inser


def InsDel(name):
	if name > 0:
		return 'Insertion'
	elif name <= 0:
		return 'Deletion'


df2['SVtype'] = df2['Size'].apply(InsDel)
print df2.head(5)


SV_count = pd.crosstab(index=df2['SVtype'], columns="count")
print SV_count


# Step 3: Merge Insertion and Deletion Tables
df = df.drop(['length'], axis=1)
new_df = pd.concat([df, df2], axis=0)
print new_df.head()
SV_count3 = pd.crosstab(index=new_df['SVtype'], columns="count")
print SV_count3
new_df.to_csv('/Users/lmc2/Desktop/NIST/Projects/ML1-TrainingData/Code/RCode/Feb42017/PythonOutput/MP.csv', index=False)


