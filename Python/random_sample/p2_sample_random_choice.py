##########################################
# Date: December 3 2017
# Description: Random sample

'''
Code
----
- random sample with pandas function
- Alternative for selecting weighted random sample 
- Run code with and without virtualenv
- !!! Revision : for a weighted sample, just pass in the count to df.sample
- Documentation : https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.sample.html
'''

##########################################



"""
Imports
"""
import pandas as pd
import numpy as np
# import graphviz
import io
import random
# from fancyimpute import KNN
# import matplotlib.pyplot as plt
from sklearn import preprocessing



'''
Data
''' 

# Import Training Data
# SVanalyzer generated training data
df_train = pd.read_csv('/Volumes/lesleydata/SVanalyzer_ML/Oct272017_ML_w_AllTech/data/train_test_data/train_data_min1.csv')
df_train_2 = pd.read_csv('/Volumes/lesleydata/SVanalyzer_ML/Oct272017_ML_w_AllTech/data/train_test_data/train_data_min1.csv')
df_train.rename(columns={'size': 'Size'}, inplace=True)


# Import Test Data
# SVanalyzer generated training data
df_test = pd.read_csv('/Volumes/lesleydata/SVanalyzer_ML/Oct272017_ML_w_AllTech/data/train_test_data/test_data_min1.csv')
df_test_2 = pd.read_csv('/Volumes/lesleydata/SVanalyzer_ML/Oct272017_ML_w_AllTech/data/train_test_data/test_data_min1.csv')
df_test.rename(columns={'size': 'Size'}, inplace=True)
df_test.head(1)

### Drop columns that are not shared by both dataframes
df_train.drop(['Label'], axis=1, inplace = True)
df_train.drop(['GTconswithoutIll300x.GT'], axis=1, inplace = True)
df_train.drop(['GTconswithoutIll250.GT'], axis=1, inplace = True)
df_train.drop(['GTconswithoutIllMP.GT'], axis=1, inplace = True)
df_train.drop(['GTconswithoutTenX.GT'], axis=1, inplace = True)
df_train.drop(['GTconswithoutpacbio.GT'], axis=1, inplace = True)
# df_train.drop(['Ill300x.GT'], axis=1, inplace = True)
# df_train.drop(['Ill250.GT'], axis=1, inplace = True)
# df_train.drop(['IllMP.GT'], axis=1, inplace = True)
# df_train.drop(['TenX.GT'], axis=1, inplace = True)
# df_train.drop(['pacbio.GT'], axis=1, inplace = True)
# # df_train.drop(['GTconflict'], axis=1, inplace = True)
# # df_train.drop(['GTsupp'], axis=1, inplace = True)
# df_train.drop(['sample'], axis=1, inplace = True)
# df_train.drop(['SVtype'], axis=1, inplace = True)
# df_train.drop(['type'], axis=1, inplace = True)
# # df_train.drop(['id'], axis=1, inplace = True)
# df_train.drop(['Label'], axis=1, inplace = True)

### Drop Columns
### Drop columns that are not shared by both dataframes
# df_test.drop(['Ill300x.amb_reason_alignmentScore_insertSizeScore'], axis=1, inplace = True)
df_test.drop(['Ill300x.amb_reason_insertSizeScore_orientation'], axis=1, inplace = True)
df_test.drop(['Ill300x.amb_reason_orientation_insertSizeScore'], axis=1, inplace = True)
df_test.drop(['Ill250.amb_reason_insertSizeScore_insertSizeScore'], axis=1, inplace = True)
df_test.drop(['Ill250.amb_reason_insertSizeScore_orientation'], axis=1, inplace = True)
df_test.drop(['IllMP.amb_reason_orientation_insertSizeScore'], axis=1, inplace = True)
df_test.drop(['TenX.HP1_amb_reason_insertSizeScore_insertSizeScore'], axis=1, inplace = True)
df_test.drop(['TenX.HP1_amb_reason_insertSizeScore_orientation'], axis=1, inplace = True)
df_test.drop(['TenX.HP1_amb_reason_orientation_insertSizeScore'], axis=1, inplace = True)
df_test.drop(['TenX.HP1_ref_reason_insertSizeScore'], axis=1, inplace = True)
df_test.drop(['TenX.HP2_amb_reason_insertSizeScore_insertSizeScore'], axis=1, inplace = True)
df_test.drop(['TenX.HP2_amb_reason_insertSizeScore_orientation'], axis=1, inplace = True)
df_test.drop(['TenX.HP2_amb_reason_orientation_insertSizeScore'], axis=1, inplace = True)
df_test.drop(['TenX.HP2_ref_reason_insertSizeScore'], axis=1, inplace = True)
df_test.drop(['GTconswithoutIll300x.GT'], axis=1, inplace = True)
df_test.drop(['GTconswithoutIll250.GT'], axis=1, inplace = True)
df_test.drop(['GTconswithoutIllMP.GT'], axis=1, inplace = True)
df_test.drop(['GTconswithoutTenX.GT'], axis=1, inplace = True)
df_test.drop(['GTconswithoutpacbio.GT'], axis=1, inplace = True)
# df_test.drop(['Ill300x.GT'], axis=1, inplace = True)
# df_test.drop(['Ill250.GT'], axis=1, inplace = True)
# df_test.drop(['IllMP.GT'], axis=1, inplace = True)
# df_test.drop(['TenX.GT'], axis=1, inplace = True)
# df_test.drop(['pacbio.GT'], axis=1, inplace = True)
# # df_test.drop(['GTcons'], axis=1, inplace = True)
# df_test.drop(['GTconflict'], axis=1, inplace = True)
# df_test.drop(['GTsupp'], axis=1, inplace = True)
# df_test.drop(['sample'], axis=1, inplace = True)
# df_test.drop(['SVtype'], axis=1, inplace = True)
# df_test.drop(['type'], axis=1, inplace = True)
# df_test.drop(['id'], axis=1, inplace = True)


# print (pd.value_counts(df_train['GTcons'].values, sort=False))

df_train['chrom'].replace('X', 23, inplace=True)
df_train['chrom'].replace('Y', 24, inplace=True)
df_test['chrom'].replace('X', 23, inplace=True)
df_test['chrom'].replace('Y', 24, inplace=True)


# Assign new ID to dataframe
# Check for random sample [look for a mix of IDs]
# Separate randomly selected group from remaining data
horizontal = pd.concat([df_train, df_test], axis=0)
horizontal = horizontal.reset_index()
horizontal['New_ID'] = horizontal.index + 880
horizontal.to_csv('/Volumes/lesleydata/RF_model_trainingData_test/combined_data.csv', index=False)

'''
NOTE
----
Numpy random sample has no 'weighted' feature, must select number of values to be 
selected from each group prior to random.sample
'''


'''
Step 1
------
Find the number of each GT that should be randomly sampled
Rationale : Dataset does not have equal numbers of each GT
Use: random.choices
Must be run in a Python 3.6 env
'''
# r = ['0', '1', '2']
# row = random.choices(r, weights=[1850, 2864, 1121], k=2750)
# # df_new = horizontal.ix[row]
# # df_new_2 = df_new.drop_duplicates()
# df2 = pd.DataFrame()
# df2['GTcons'] = row
# print (pd.value_counts(df2['GTcons'].values, sort=False))



'''
Step 2
------
Randomly sample from each GT 
Run outside of Virtualenv (ie - run with Python 2.7)
'''

# Will use a string based selection - must convert all of GTcons to strings

homRef_samp2 = horizontal.sample(2750)
# homRef_samp2 = homRef_samp.sample(867)
# hetVar_samp2 = hetVar_samp.sample(1379)
# homVar_samp2 = homVar_samp.sample(504)
all_ = homRef_samp2
all_ = all_.drop_duplicates()
print (all_.shape)
print (pd.value_counts(all_['GTcons'].values, sort=False))

keep = all_['New_ID']
df_testSet = horizontal[~horizontal['New_ID'].isin(keep)]
print(horizontal.shape)
print(df_testSet.shape)
all_.to_csv('/Volumes/lesleydata/RF_model_trainingData_test/train/random_sample_AllData_szwt_train.csv', index=False)
df_testSet.to_csv('/Volumes/lesleydata/RF_model_trainingData_test/test/random_sample_AllData_szwt_test.csv', index=False)


'''
Step 2
------
Randomly sample from each GT 
Run outside of Virtualenv (ie - run with Python 2.7)
'''

# Will use a string based selection - must convert all of GTcons to strings
horizontal['GTcons'].replace(0, 'Homozygous_Reference', inplace=True)
horizontal['GTcons'].replace(1, 'Heterozygous_Variant', inplace=True)
horizontal['GTcons'].replace(2, 'Homozygous_Variant', inplace=True)

df_homRef = horizontal[horizontal['GTcons'].str.contains('Homozygous_Reference')]
df_hetVar = horizontal[horizontal['GTcons'].str.contains('Heterozygous_Variant')]
df_homVar = horizontal[horizontal['GTcons'].str.contains('Homozygous_Variant')]

homRef_samp = pd.DataFrame(df_homRef)
hetVar_samp = pd.DataFrame(df_hetVar)
homVar_samp = pd.DataFrame(df_homVar)

homRef_samp2 = homRef_samp.sample(867)
hetVar_samp2 = hetVar_samp.sample(1379)
homVar_samp2 = homVar_samp.sample(504)
all_ = pd.concat([homRef_samp2, hetVar_samp2, homVar_samp2], axis=0)
all_ = all_.drop_duplicates()
print (all_.shape)
print (pd.value_counts(all_['GTcons'].values, sort=False))

keep = all_['New_ID']
df_testSet = horizontal[~horizontal['New_ID'].isin(keep)]
print(horizontal.shape)
print(df_testSet.shape)
all_.to_csv('/Volumes/lesleydata/RF_model_trainingData_test/train/random_sample_AllData_szwt_train_.csv', index=False)
df_testSet.to_csv('/Volumes/lesleydata/RF_model_trainingData_test/test/random_sample_AllData_szwt_test_.csv', index=False)




