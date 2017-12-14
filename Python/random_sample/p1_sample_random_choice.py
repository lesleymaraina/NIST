#################################################
# Date : December 3 2017
# Description : Determine weighted count 
'''
- Must run in a python 3.6+ env
- Use virtualenv py2
'''
#################################################
import pandas as pd
import numpy as np
import io
import random
from sklearn import preprocessing

r = ['-1','0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54']
row = random.choices(r, weights=[435, 27, 30, 50, 222, 500, 637, 235, 15, 24, 41, 26, 816, 143, 114, 652, 15, 100, 24, 46, 91, 40, 396, 11, 172, 42, 11, 49, 16, 69, 14, 28, 12, 77, 10, 16, 10, 30, 72, 12, 13, 11, 26, 40, 16, 21, 14, 21, 91, 19, 67, 12, 64, 56, 23, 11,], k=2750)
df2 = pd.DataFrame(row)


df2['Num_Analysis'] = row
df4 = pd.value_counts(df2['Num_Analysis'].values, sort=False)
df5 = pd.DataFrame(df4)
df5['ClusterID'] = df4.index
df5.rename(columns={0: 'Cluster_Count'}, inplace=True)
df5.to_csv('df123.csv', index=False)
