###########################################
# Imports
###########################################
import pandas as pd
import numpy as np
from fancyimpute import KNN
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import LeaveOneOut
from scipy.stats import ks_2samp
from scipy import stats
from matplotlib import pyplot

df = pd.read_csv("/Users/lmc2/Desktop/NIST/Projects/ML1-TrainingData/Code/PythonCode/Feb132017/ML.Training/svvizAllData.DEL.csv")


###########################################
# Convert Categorical to Numerical
########################################### 
#Label Encoding: convert categorical to numerical
label_encoder = preprocessing.LabelEncoder()
df['chrom'] = label_encoder.fit_transform(df['chrom'])
df['SVtype'] = label_encoder.fit_transform(df['SVtype'])
df['sample'] = label_encoder.fit_transform(df['sample'])
df['type'] = label_encoder.fit_transform(df['type'])
print df.head(4)

# Count Number of NaN in each column
NaN_count = df.isnull().sum()
print NaN_count

###########################################
# KNN to impute missing value
########################################### 

#Convert dataframe to matrix
X = df.as_matrix()

# Imput missing values from three closest observations
X_imputed = KNN(k=3).complete(X)
df2 = pd.DataFrame(X_imputed)

#Re-label all columns in the dataframe
df2.columns = ['chrom',
'start',
'end',
'sample',
'id',
'type',
'SVtype',
'Size',
'Ill300x.alt_alnScore_mean',
'Ill300x.alt_alnScore_std',
'Ill300x.alt_count',
'Ill300x.alt_insertSize_mean',
'Ill300x.alt_insertSize_std',
'Ill300x.alt_reason_alignmentScore',
'Ill300x.alt_reason_insertSizeScore',
'Ill300x.alt_reason_orientation',
'Ill300x.amb_alnScore_mean',
'Ill300x.amb_alnScore_std',
'Ill300x.amb_count',
'Ill300x.amb_insertSize_mean',
'Ill300x.amb_insertSize_std',
'Ill300x.amb_reason_alignmentScore_alignmentScore',
'Ill300x.amb_reason_alignmentScore_orientation',
'Ill300x.amb_reason_flanking',
'Ill300x.amb_reason_insertSizeScore_alignmentScore',
'Ill300x.amb_reason_insertSizeScore_insertSizeScore',
'Ill300x.amb_reason_insertSizeScore_orientation',
'Ill300x.amb_reason_multimapping',
'Ill300x.amb_reason_orientation_alignmentScore',
'Ill300x.amb_reason_orientation_orientation',
'Ill300x.amb_reason_same_scores',
'Ill300x.ref_alnScore_mean',
'Ill300x.ref_alnScore_std',
'Ill300x.ref_count',
'Ill300x.ref_insertSize_mean',
'Ill300x.ref_insertSize_std',
'Ill300x.ref_reason_alignmentScore',
'Ill300x.ref_reason_insertSizeScore',
'Ill300x.ref_reason_orientation',
'Ill300x.GT',
'Ill250.alt_alnScore_mean',
'Ill250.alt_alnScore_std',
'Ill250.alt_count',
'Ill250.alt_insertSize_mean',
'Ill250.alt_insertSize_std',
'Ill250.alt_reason_alignmentScore',
'Ill250.alt_reason_insertSizeScore',
'Ill250.alt_reason_orientation',
'Ill250.amb_alnScore_mean',
'Ill250.amb_alnScore_std',
'Ill250.amb_count',
'Ill250.amb_insertSize_mean',
'Ill250.amb_insertSize_std',
'Ill250.amb_reason_alignmentScore_alignmentScore',
'Ill250.amb_reason_alignmentScore_orientation',
'Ill250.amb_reason_flanking',
'Ill250.amb_reason_insertSizeScore_alignmentScore',
'Ill250.amb_reason_insertSizeScore_insertSizeScore',
'Ill250.amb_reason_insertSizeScore_orientation',
'Ill250.amb_reason_multimapping',
'Ill250.amb_reason_orientation_alignmentScore',
'Ill250.amb_reason_orientation_orientation',
'Ill250.amb_reason_same_scores',
'Ill250.ref_alnScore_mean',
'Ill250.ref_alnScore_std',
'Ill250.ref_count',
'Ill250.ref_insertSize_mean',
'Ill250.ref_insertSize_std',
'Ill250.ref_reason_alignmentScore',
'Ill250.ref_reason_insertSizeScore',
'Ill250.ref_reason_orientation',
'Ill250.GT',
'IllMP.alt_alnScore_mean',
'IllMP.alt_alnScore_std',
'IllMP.alt_count',
'IllMP.alt_insertSize_mean',
'IllMP.alt_insertSize_std',
'IllMP.alt_reason_alignmentScore',
'IllMP.alt_reason_insertSizeScore',
'IllMP.alt_reason_orientation',
'IllMP.amb_alnScore_mean',
'IllMP.amb_alnScore_std',
'IllMP.amb_count',
'IllMP.amb_insertSize_mean',
'IllMP.amb_insertSize_std',
'IllMP.amb_reason_alignmentScore_alignmentScore',
'IllMP.amb_reason_alignmentScore_orientation',
'IllMP.amb_reason_flanking',
'IllMP.amb_reason_insertSizeScore_alignmentScore',
'IllMP.amb_reason_insertSizeScore_insertSizeScore',
'IllMP.amb_reason_multimapping',
'IllMP.amb_reason_orientation_alignmentScore',
'IllMP.amb_reason_orientation_orientation',
'IllMP.amb_reason_same_scores',
'IllMP.ref_alnScore_mean',
'IllMP.ref_alnScore_std',
'IllMP.ref_count',
'IllMP.ref_insertSize_mean',
'IllMP.ref_insertSize_std',
'IllMP.ref_reason_alignmentScore',
'IllMP.ref_reason_insertSizeScore',
'IllMP.ref_reason_orientation',
'IllMP.GT',
'TenX.HP1_alt_alnScore_mean',
'TenX.HP1_alt_alnScore_std',
'TenX.HP1_alt_count',
'TenX.HP1_alt_insertSize_mean',
'TenX.HP1_alt_insertSize_std',
'TenX.HP1_alt_reason_alignmentScore',
'TenX.HP1_alt_reason_insertSizeScore',
'TenX.HP1_alt_reason_orientation',
'TenX.HP1_amb_alnScore_mean',
'TenX.HP1_amb_alnScore_std',
'TenX.HP1_amb_count',
'TenX.HP1_amb_insertSize_mean',
'TenX.HP1_amb_insertSize_std',
'TenX.HP1_amb_reason_alignmentScore_alignmentScore',
'TenX.HP1_amb_reason_alignmentScore_orientation',
'TenX.HP1_amb_reason_flanking',
'TenX.HP1_amb_reason_insertSizeScore_alignmentScore',
'TenX.HP1_amb_reason_insertSizeScore_insertSizeScore',
'TenX.HP1_amb_reason_insertSizeScore_orientation',
'TenX.HP1_amb_reason_multimapping',
'TenX.HP1_amb_reason_orientation_alignmentScore',
'TenX.HP1_amb_reason_orientation_insertSizeScore',
'TenX.HP1_amb_reason_orientation_orientation',
'TenX.HP1_amb_reason_same_scores',
'TenX.HP1_ref_alnScore_mean',
'TenX.HP1_ref_alnScore_std',
'TenX.HP1_ref_count',
'TenX.HP1_ref_insertSize_mean',
'TenX.HP1_ref_insertSize_std',
'TenX.HP1_ref_reason_alignmentScore',
'TenX.HP1_ref_reason_insertSizeScore',
'TenX.HP1_ref_reason_orientation',
'TenX.HP2_alt_alnScore_mean',
'TenX.HP2_alt_alnScore_std',
'TenX.HP2_alt_count',
'TenX.HP2_alt_insertSize_mean',
'TenX.HP2_alt_insertSize_std',
'TenX.HP2_alt_reason_alignmentScore',
'TenX.HP2_alt_reason_insertSizeScore',
'TenX.HP2_alt_reason_orientation',
'TenX.HP2_amb_alnScore_mean',
'TenX.HP2_amb_alnScore_std',
'TenX.HP2_amb_count',
'TenX.HP2_amb_insertSize_mean',
'TenX.HP2_amb_insertSize_std',
'TenX.HP2_amb_reason_alignmentScore_alignmentScore',
'TenX.HP2_amb_reason_alignmentScore_orientation',
'TenX.HP2_amb_reason_flanking',
'TenX.HP2_amb_reason_insertSizeScore_alignmentScore',
'TenX.HP2_amb_reason_insertSizeScore_insertSizeScore',
'TenX.HP2_amb_reason_multimapping',
'TenX.HP2_amb_reason_orientation_alignmentScore',
'TenX.HP2_amb_reason_orientation_insertSizeScore',
'TenX.HP2_amb_reason_orientation_orientation',
'TenX.HP2_amb_reason_same_scores',
'TenX.HP2_ref_alnScore_mean',
'TenX.HP2_ref_alnScore_std',
'TenX.HP2_ref_count',
'TenX.HP2_ref_insertSize_mean',
'TenX.HP2_ref_insertSize_std',
'TenX.HP2_ref_reason_alignmentScore',
'TenX.HP2_ref_reason_insertSizeScore',
'TenX.HP2_ref_reason_orientation',
'TenX.GT',
'pacbio.alt_alnScore_mean',
'pacbio.alt_alnScore_std',
'pacbio.alt_count',
'pacbio.alt_insertSize_mean',
'pacbio.alt_insertSize_std',
'pacbio.alt_reason_alignmentScore',
'pacbio.amb_alnScore_mean',
'pacbio.amb_alnScore_std',
'pacbio.amb_count',
'pacbio.amb_insertSize_mean',
'pacbio.amb_insertSize_std',
'pacbio.amb_reason_alignmentScore_alignmentScore',
'pacbio.amb_reason_flanking',
'pacbio.amb_reason_multimapping',
'pacbio.amb_reason_same_scores',
'pacbio.ref_alnScore_mean',
'pacbio.ref_alnScore_std',
'pacbio.ref_count',
'pacbio.ref_insertSize_mean',
'pacbio.ref_insertSize_std',
'pacbio.ref_reason_alignmentScore',
'pacbio.GT',
'GTcons',
'GTconflict',
'GTsupp']


# Count NaNs post KNN imputation
print df2.head(4)
NaN_count = df2.isnull().sum()
print NaN_count

d2.to_csv('svvizAllData.DEL.nan.csv', index=False)

###########################################
# KS Test 
########################################### 
# Confirm distribution of KNN imputed column
# Notes:
# test is designed to find alpha, the probability of Type I error
# test only really lets you speak of your confidence that the distributions are different, not the same
# null-hypothesis for the KS test is that the distributions are the same
# the lower your p value the greater the statistical evidence you have to reject the null hypothesis and conclude the distributions are different
pre = df['Ill300x.alt_alnScore_std']
post = df2['Ill300x.alt_alnScore_std']
pre = pre.as_matrix()
post = post.as_matrix()

comp = ks_2samp(pre, post)
print ('Distribution comparison for Ill300x.alt_alnScore_std: {}'.format(comp))

pre = df['pacbio.alt_alnScore_mean']
post = df2['pacbio.alt_alnScore_mean']
pre = pre.as_matrix()
post = post.as_matrix()
comp = ks_2samp(pre, post)
print ('Distribution comparison for pacbio.alt_alnScore_mean: {}'.format(comp))

pre = df['TenX.HP2_ref_reason_alignmentScore']
post = df2['TenX.HP2_ref_reason_alignmentScore']
pre = pre.as_matrix()
post = post.as_matrix()
comp = ks_2samp(pre, post)
print ('Distribution comparison for TenX.HP2_ref_reason_alignmentScore: {}'.format(comp))

# Plot distributions on the same graph?

###########################################
# KNN: additional strategies
########################################### 
#Leave one out 
loo = LeaveOneOut()
# for train_index, test_index in loo.split(X):



# #source: http://chrisalbon.com/machine-learning/impute_missing_values_with_k-nearest_neighbors.html
# #Encoder Example: http://machinelearningmastery.com/data-preparation-gradient-boosting-xgboost-python/