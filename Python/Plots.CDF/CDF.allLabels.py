##################################################
# About
# Date: June 1 2017
# Description
# Summarize DSCAN labels:
# Create histograms and CDF plots 
##################################################

##################################################
# Import
##################################################
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

##################################################
# Data
##################################################
# DBSCAN/tSNE data
df = pd.read_csv('/Volumes/lesleydata/SVVIZOutput/April112017/Step4/MachineLearning/Step3.tSNE/INS.tSNE.raw.csv')
lab = df['clusterLabel']
lab.SVD = df['clusterLabel.SVD']
lab.raw = df['clusterLabel.raw']


##################################################
# DBSCAN/tSNE
##################################################

'''
1. List the counts of each label
2. Plot Frequency of each label in a histogram
'''
counting = df.groupby('clusterLabel').count()
countr = df['clusterLabel'].value_counts()
print (countr)
plt.hist(lab, bins=96, color='c')
plt.title("DBSCAN Cluster Label Counts")
plt.xlabel("Cluster Label")
plt.ylabel("Frequency")
plt.axhline(y=125)
plt.show()


'''
3. Plot cumulative distribution function
'''

# sort the data:
data_sorted = np.sort(df['clusterLabel'])

# calculate the proportional values of samples
p = 1. * np.arange(len(df['clusterLabel'])) / (len(df['clusterLabel']) - 1)

# plot the sorted data:
_ = plt.plot(data_sorted, p, marker='.', linestyle='none')
_ = plt.xlabel('x')
_ = plt.ylabel('y')
plt.margins(0.02)
plt.show()


##################################################
# DBSCAN/SVD
##################################################

'''
1. List the counts of each label
2. Plot Frequency of each label in a histogram
'''
counting = df.groupby('clusterLabel.SVD').count()
countr = df['clusterLabel.SVD'].value_counts()
print (countr)
plt.hist(lab.SVD, bins=16, color='c')
plt.title("DBSCAN/SVD Cluster Label Counts")
plt.xlabel("SVD Cluster Label")
plt.ylabel("Frequency")
plt.axhline(y=125)
plt.show()


'''
3. Plot cumulative distribution function
'''

# sort the data:
data_sorted = np.sort(df['clusterLabel.SVD'])

# calculate the proportional values of samples
p = 1. * np.arange(len(df['clusterLabel.SVD'])) / (len(df['clusterLabel.SVD']) - 1)

# plot the sorted data:
_ = plt.plot(data_sorted, p, marker='.', linestyle='none')
_ = plt.xlabel('x')
_ = plt.ylabel('y')
plt.margins(0.02)
plt.show()


##################################################
# DBSCAN/raw data
##################################################

'''
1. List the counts of each label
2. Plot Frequency of each label in a histogram
'''
counting = df.groupby('clusterLabel.raw').count()
countr = df['clusterLabel.raw'].value_counts()
print (countr)
plt.hist(lab.raw, bins=96, color='c')
plt.title("DBSCAN/Raw Data Cluster Label Counts")
plt.xlabel("Cluster Label")
plt.ylabel("Frequency")
plt.axhline(y=125)
plt.show()


'''
3. Plot cumulative distribution function
'''

# sort the data:
data_sorted = np.sort(df['clusterLabel.raw'])

# calculate the proportional values of samples
p = 1. * np.arange(len(df['clusterLabel.raw'])) / (len(df['clusterLabel.raw']) - 1)

# plot the sorted data:
_ = plt.plot(data_sorted, p, marker='.', linestyle='none')
_ = plt.xlabel('x')
_ = plt.ylabel('y')
plt.margins(0.02)
plt.show()


