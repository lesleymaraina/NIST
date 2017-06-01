##################################################
# Import
##################################################
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

##################################################
# Data
##################################################

df = pd.read_csv('/Volumes/lesleydata/SVVIZOutput/April112017/Step4/MachineLearning/Step3.tSNE/INS.tSNE.csv')
lab = df['clusterLabel']

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


# x = np.sort(df['clusterLabel'])
# y = np.arange(1, len(x)+1) / len(x)
# _ = plt.plot(x,y, marker='.', linestyle='none')
# _ = plt.xlabel('DBSCAN Cluster Number')
# _ = plt.ylabel('frequency')
# plt.margins(0.02)
# plt.show()



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


