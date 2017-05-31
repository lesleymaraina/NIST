import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt


df = pd.read_csv('/Volumes/lesleydata/SVVIZOutput/April112017/Step4/MachineLearning/Step3.tSNE/INS.tSNE.csv')
lab = df['clusterLabel']
counting = df.groupby('clusterLabel').count()
countr = df['clusterLabel'].value_counts()
print (countr)
plt.hist(lab, bins=96, color='c')
plt.title("DBSCAN Cluster Label Counts")
plt.xlabel("Cluster Label")
plt.ylabel("Frequency")
plt.axhline(y=125)
plt.show()


x = np.sort(df['clusterLabel'])
y = np.arange(1, len(x)+1) / len(x)
_ = plt.plot(x,y, marker='.', linestyle='none')
_ = plt.xlabel('DBSCAN Cluster Number')
_ = plt.ylabel('frequency')
plt.margins(0.02)
plt.show()



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

# fig = figure()
# ax1 = fig.add_subplot(121)
# ax1.plot(p, data_sorted)
# ax1.set_xlabel('$p$')
# ax1.set_ylabel('$x$')

# ax2 = fig.add_subplot(122)
# ax2.plot(data_sorted, p)
# ax2.set_xlabel('$x$')
# ax2.set_ylabel('$p$')
