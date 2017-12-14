##########################################
# Date: December 3 2017
# Description: Random sample

'''
Code
----
- random sample with pandas function
- Alternative for selecting weighted random sample 
- Run code with and without virtualenv
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
all_.to_csv('/Volumes/lesleydata/RF_model_trainingData_test/train/random_sample_AllData_szwt_train.csv', index=False)
df_testSet.to_csv('/Volumes/lesleydata/RF_model_trainingData_test/test/random_sample_AllData_szwt_test.csv', index=False)

'''
Step 3
------
Randomly sample from each size group 
Run outside of Virtualenv (ie - run with Python 2.7)
'''

# horizontal = pd.concat([df_train, df_test], axis=0)
# horizontal = horizontal.reset_index()
# horizontal['New_ID'] = horizontal.index + 880


#Size Bins
bins = [0,19, 50,100,300,400,500,1000,5999,500000]
horizontal['Size'] = horizontal['Size'].abs()
group_names_size = ['0-20', '20-50', '50-100', '100-300', '300-400', '400-500', '500-1000', '1000-5999', '6000+']
horizontal['size_bin'] = pd.cut(horizontal['Size'], bins, labels=group_names_size)
horizontal['size_bin'] = horizontal.size_bin.astype(str)
print (pd.value_counts(horizontal['size_bin'].values, sort=False))

horizontal.to_csv('hor_sizeBin.csv', index=False)



df_20to50 = horizontal[horizontal['size_bin'].str.contains('20-50')]
df_50to100 = horizontal[horizontal['size_bin'].str.contains('50-100')]
df_100to300 = horizontal[horizontal['size_bin'].str.contains('100-300')]
df_300to400 = horizontal[horizontal['size_bin'].str.contains('300-400')]
df_400to500 = horizontal[horizontal['size_bin'].str.contains('400-500')]
df_500to1000 = horizontal[horizontal['size_bin'].str.contains('500-1000')]
df_1000to6000 = horizontal[horizontal['size_bin'].str.contains('1000-5999')]
df_6000 = horizontal[horizontal['size_bin'].str.contains('6000+')]


df_20to50_ = pd.DataFrame(df_20to50)
df_50to100_ = pd.DataFrame(df_50to100)
df_100to300_ = pd.DataFrame(df_100to300)
df_300to400_ = pd.DataFrame(df_300to400)
df_400to500_ = pd.DataFrame(df_400to500)
df_500to1000_ = pd.DataFrame(df_500to1000)
df_1000to6000_ = pd.DataFrame(df_1000to6000)
df_6000_ = pd.DataFrame(df_6000)
df3 = pd.concat([df_20to50_, df_50to100_, df_100to300_, df_300to400_, df_400to500_, df_500to1000_, df_1000to6000_, df_6000_], axis=0)
df3.to_csv('/Volumes/lesleydata/RF_model_trainingData_test/train/all_size_bins.csv', index=False)

# r = ['20to50', '50to100', '100to300', '300to400', '400to500', '500to1000', '1000to6000', '6000']
# row = random.choices(r, weights=[3388, 861, 595, 495, 53, 124, 227, 57], k=2750)
# # df_new = horizontal.ix[row]
# # df_new_2 = df_new.drop_duplicates()
# df2 = pd.DataFrame()
# df2['GTcons'] = row
# print (pd.value_counts(df2['GTcons'].values, sort=False))

# The numbers below are from the 'random.choices' code above
# This is a weighted selection of the number of each category that should be included in the analysis
df_20to50_2 = df_20to50_.sample(1599)
df_50to100_2 = df_50to100_.sample(407)
df_100to300_2 = df_100to300_.sample(259)
df_300to400_2 = df_300to400_.sample(227)
df_400to500_2 = df_400to500_.sample(33)
df_500to1000_2 = df_500to1000_.sample(83)
df_1000to6000_2 = df_1000to6000_.sample(115)
df_6000_2 = df_6000_.sample(27)

all_ = pd.concat([df_20to50_2, df_50to100_2, df_100to300_2, df_300to400_2, df_400to500_2, df_500to1000_2, df_1000to6000_2, df_6000_2], axis=0)
all_ = all_.drop_duplicates()
print (all_.shape)
print (pd.value_counts(all_['GTcons'].values, sort=False))

keep = all_['New_ID']
df_testSet = horizontal[~horizontal['New_ID'].isin(keep)]


print(horizontal.shape)
print(df_testSet.shape)
all_.to_csv('/Volumes/lesleydata/RF_model_trainingData_test/train/random_sample_SizeBins_szwt_train.csv', index=False)
df_testSet.to_csv('/Volumes/lesleydata/RF_model_trainingData_test/test/random_sample_SizeBins_szwt_test.csv', index=False)

'''
Step 4
------
Randomly sample from tSNE Clusters
Run outside of Virtualenv (ie - run with Python 2.7)
'''

df = pd.read_csv('/Volumes/lesleydata/RF_model_trainingData_test/Data_Cluster.csv')
df['Cluster_Labels'] = df.Cluster_Labels.astype(str)

# horizontal = horizontal.reset_index()
# df['counter'] = range(len(df))
# horizontal['New_ID'] = horizontal.index + 880

df = df.reset_index()
df['New_ID_'] = range(len(df))

# print (pd.value_counts(df['Cluster_Labels'].values, sort=False))


# df_min1 = df[df['Cluster_Count'].str.contains('-1')]
df_0 = df[df['Cluster_Labels'].str.contains('0')]
df_1 = df[df['Cluster_Labels'].str.contains('1')]
df_2 = df[df['Cluster_Labels'].str.contains('2')]
df_3 = df[df['Cluster_Labels'].str.contains('3')]
df_4 = df[df['Cluster_Labels'].str.contains('4')]
df_5 = df[df['Cluster_Labels'].str.contains('5')]
df_6 = df[df['Cluster_Labels'].str.contains('6')]
df_7 = df[df['Cluster_Labels'].str.contains('7')]
df_8 = df[df['Cluster_Labels'].str.contains('8')]
df_9 = df[df['Cluster_Labels'].str.contains('9')]
df_10 = df[df['Cluster_Labels'].str.contains('10')]
df_11 = df[df['Cluster_Labels'].str.contains('11')]
df_12 = df[df['Cluster_Labels'].str.contains('12')]
df_13 = df[df['Cluster_Labels'].str.contains('13')]
df_14 = df[df['Cluster_Labels'].str.contains('14')]
df_15 = df[df['Cluster_Labels'].str.contains('15')]
df_16 = df[df['Cluster_Labels'].str.contains('16')]
df_17 = df[df['Cluster_Labels'].str.contains('17')]
df_18 = df[df['Cluster_Labels'].str.contains('18')]
df_19 = df[df['Cluster_Labels'].str.contains('19')]
df_20 = df[df['Cluster_Labels'].str.contains('20')]
df_21 = df[df['Cluster_Labels'].str.contains('21')]
df_22 = df[df['Cluster_Labels'].str.contains('22')]
df_23 = df[df['Cluster_Labels'].str.contains('23')]
df_24 = df[df['Cluster_Labels'].str.contains('24')]
df_25 = df[df['Cluster_Labels'].str.contains('25')]
df_26 = df[df['Cluster_Labels'].str.contains('26')]
df_27 = df[df['Cluster_Labels'].str.contains('27')]
df_28 = df[df['Cluster_Labels'].str.contains('28')]
df_29 = df[df['Cluster_Labels'].str.contains('29')]
df_30 = df[df['Cluster_Labels'].str.contains('30')]
df_31 = df[df['Cluster_Labels'].str.contains('31')]
df_32 = df[df['Cluster_Labels'].str.contains('32')]
df_33 = df[df['Cluster_Labels'].str.contains('33')]
df_34 = df[df['Cluster_Labels'].str.contains('34')]
df_35 = df[df['Cluster_Labels'].str.contains('35')]
df_36 = df[df['Cluster_Labels'].str.contains('36')]
df_37 = df[df['Cluster_Labels'].str.contains('37')]
df_38 = df[df['Cluster_Labels'].str.contains('38')]
df_39 = df[df['Cluster_Labels'].str.contains('39')]
df_40 = df[df['Cluster_Labels'].str.contains('40')]
df_41 = df[df['Cluster_Labels'].str.contains('41')]
df_42 = df[df['Cluster_Labels'].str.contains('42')]
df_43 = df[df['Cluster_Labels'].str.contains('43')]
df_44 = df[df['Cluster_Labels'].str.contains('44')]
df_45 = df[df['Cluster_Labels'].str.contains('45')]
df_46 = df[df['Cluster_Labels'].str.contains('46')]
df_47 = df[df['Cluster_Labels'].str.contains('47')]
df_48 = df[df['Cluster_Labels'].str.contains('48')]
df_49 = df[df['Cluster_Labels'].str.contains('49')]
df_50 = df[df['Cluster_Labels'].str.contains('50')]
df_51 = df[df['Cluster_Labels'].str.contains('51')]
df_52 = df[df['Cluster_Labels'].str.contains('52')]
df_53 = df[df['Cluster_Labels'].str.contains('53')]
df_54 = df[df['Cluster_Labels'].str.contains('54')]


# df_min1_ = pd.DataFrame(df_min1)
# print (df_min1_.shape)
df_0_ = pd.DataFrame(df_0)
df_1_ = pd.DataFrame(df_1)
df_2_ = pd.DataFrame(df_2)
df_3_ = pd.DataFrame(df_3)
df_4_ = pd.DataFrame(df_4)
df_5_ = pd.DataFrame(df_5)
df_6_ = pd.DataFrame(df_6)
df_7_ = pd.DataFrame(df_7)
df_8_ = pd.DataFrame(df_8)
df_9_ = pd.DataFrame(df_9)
df_10_ = pd.DataFrame(df_10)  
df_11_ = pd.DataFrame(df_11)  
df_12_ = pd.DataFrame(df_12)  
df_13_ = pd.DataFrame(df_13)  
df_14_ = pd.DataFrame(df_14)  
df_15_ = pd.DataFrame(df_15)  
df_16_ = pd.DataFrame(df_16)  
df_17_ = pd.DataFrame(df_17)  
df_18_ = pd.DataFrame(df_18)  
df_19_ = pd.DataFrame(df_19)  
df_20_ = pd.DataFrame(df_20)  
df_21_ = pd.DataFrame(df_21)  
df_22_ = pd.DataFrame(df_22)  
df_23_ = pd.DataFrame(df_23)  
df_24_ = pd.DataFrame(df_24)  
df_25_ = pd.DataFrame(df_25)  
df_26_ = pd.DataFrame(df_26)  
df_27_ = pd.DataFrame(df_27)  
df_28_ = pd.DataFrame(df_28)  
df_29_ = pd.DataFrame(df_29)  
df_30_ = pd.DataFrame(df_30)  
df_31_ = pd.DataFrame(df_31)  
df_32_ = pd.DataFrame(df_32)  
df_33_ = pd.DataFrame(df_33)  
df_34_ = pd.DataFrame(df_34)  
df_35_ = pd.DataFrame(df_35)  
df_36_ = pd.DataFrame(df_36)  
df_37_ = pd.DataFrame(df_37)  
df_38_ = pd.DataFrame(df_38)  
df_39_ = pd.DataFrame(df_39)  
df_40_ = pd.DataFrame(df_40)  
df_41_ = pd.DataFrame(df_41)  
df_42_ = pd.DataFrame(df_42)  
df_43_ = pd.DataFrame(df_43)  
df_44_ = pd.DataFrame(df_44)  
df_45_ = pd.DataFrame(df_45)  
df_46_ = pd.DataFrame(df_46)  
df_47_ = pd.DataFrame(df_47)  
df_48_ = pd.DataFrame(df_48)  
df_49_ = pd.DataFrame(df_49)  
df_50_ = pd.DataFrame(df_50)  
df_51_ = pd.DataFrame(df_51)  
df_52_ = pd.DataFrame(df_52)  
df_53_ = pd.DataFrame(df_53)  
df_54_ = pd.DataFrame(df_54)


# _min1_ = df_min1_.sample(180)
_0_ = df_0_.sample(11)
_1_ = df_1_.sample(21)
_2_ = df_2_.sample(20)
_3_ = df_3_.sample(112)
_4_ = df_4_.sample(234)
_5_ = df_5_.sample(314)
_6_ = df_6_.sample(128)
_7_ = df_7_.sample(8)
_8_ = df_8_.sample(16)
_9_ = df_9_.sample(17)
_10_ = df_10_.sample(22)
_11_ = df_11_.sample(373)
_12_ = df_12_.sample(65)
_13_ = df_13_.sample(68)
_14_ = df_14_.sample(308)
_15_ = df_15_.sample(7)
_16_ = df_16_.sample(42)
_17_ = df_17_.sample(12)
_18_ = df_18_.sample(27)
_19_ = df_19_.sample(34)
_20_ = df_20_.sample(28)
_21_ = df_21_.sample(160)
_22_ = df_22_.sample(5)
_23_ = df_23_.sample(88)
_24_ = df_24_.sample(23)
_25_ = df_25_.sample(5)
_26_ = df_26_.sample(14)
_27_ = df_27_.sample(11)
_28_ = df_28_.sample(43)
_29_ = df_29_.sample(2)
_30_ = df_30_.sample(12)
_31_ = df_31_.sample(2)
_32_ = df_32_.sample(29)
_33_ = df_33_.sample(1)
_34_ = df_34_.sample(11)
_35_ = df_35_.sample(2)
_36_ = df_36_.sample(12)
_37_ = df_37_.sample(30)
_38_ = df_38_.sample(7)
_39_ = df_39_.sample(7)
_40_ = df_40_.sample(5)
_41_ = df_41_.sample(7)
_42_ = df_42_.sample(22)
_43_ = df_43_.sample(11)
_44_ = df_44_.sample(7)
_45_ = df_45_.sample(1)
_46_ = df_46_.sample(9)
_47_ = df_47_.sample(48)
_48_ = df_48_.sample(6)
_49_ = df_49_.sample(35)
_50_ = df_50_.sample(4)
_51_ = df_51_.sample(33)
_52_ = df_52_.sample(38)
_53_ = df_53_.sample(6)
_54_  = df_54_.sample(7)


all_ = pd.concat([_0_,_1_,_2_,_3_,_4_,_5_,_6_,_7_,_8_,_9_,_10_,_11_,_12_,_13_,_14_,_15_,_16_,_17_,_18_,_19_,_20_,_21_,_22_,_23_,_24_,_25_,_26_,_27_,_28_,_29_,_30_,_31_,_32_,_33_,_34_,_35_,_36_,_37_,_38_,_39_,_40_,_41_,_42_,_43_,_44_,_45_,_46_,_47_,_48_,_49_,_50_,_51_,_52_,_53_,_54_], axis=0)
all_ = all_.drop_duplicates()
print (all_.shape)

keep = all_['New_ID_']
df_testSet = df[~df['New_ID_'].isin(keep)]
print(df.shape)
print(all_.shape)
print(df_testSet.shape)

all_.to_csv('/Volumes/lesleydata/RF_model_trainingData_test/train/random_sample_tSNE_train.csv', index=False)
df_testSet.to_csv('/Volumes/lesleydata/RF_model_trainingData_test/test/random_sample_tSNE_test.csv', index=False)



# # FYI: Strategy 2
# homRef_samp = random.sample(homRef_samp.index, 867)
# homRef_samp = df_homRef.ix[homRef_samp]
# homRef_samp2 = homRef_samp.drop_duplicates()
# hetVar_samp = random.sample(hetVar_samp.index, 1379)
# hetVar_samp = df_hetVar.ix[hetVar_samp]
# hetVar_samp2 = hetVar_samp.drop_duplicates()
# homVar_samp = random.sample(homVar_samp.index, 504)
# homVar_samp = df_homVar.ix[homVar_samp]
# homVar_samp2 = homVar_samp.drop_duplicates()

# all_ = pd.concat([homRef_samp, hetVar_samp, homVar_samp], axis=0)
# print (homRef_samp2.shape)
# print (hetVar_samp2.shape)
# print (homVar_samp.shape)
# print (all_.shape)




