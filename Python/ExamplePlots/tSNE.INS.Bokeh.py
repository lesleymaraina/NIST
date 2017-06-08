###########################################
# About
# Resources
# http://bokeh.pydata.org/en/0.11.0/docs/user_guide/charts.html
# https://www.youtube.com/watch?v=NhTRrnLHTTc
# Many examples
# http://pbpython.com/visualization-tools-1.html

###########################################

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
from sklearn import preprocessing
from scipy.linalg import svd
from sklearn.decomposition import TruncatedSVD
import sqlite3
import seaborn as sns
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA as sklearnPCA
import plotly.plotly as py
from sklearn.cluster import DBSCAN
from ggplot import *
from bokeh.charts import Scatter, Histogram, output_file, show
# from .theme import theme
# from .theme import theme_matplotlib
# from .theme_matplotlib import theme_matplotlib
from sklearn import (manifold, datasets, decomposition, ensemble,
                     discriminant_analysis, random_projection)



df = pd.read_csv("/Volumes/lesleydata/SVVIZOutput/April112017/Step4/MachineLearning/Step1.DataCleaning.Output/INS/svviz.Annotate.INS.HG002.csv")
df4 = pd.read_csv("/Volumes/lesleydata/SVVIZOutput/April112017/Step4/MachineLearning/Step1.DataCleaning.Output/INS/svviz.Annotate.INS.HG002.csv")
log_size = pd.read_csv("/Volumes/lesleydata/SVVIZOutput/April112017/Step4/MachineLearning/Step3.tSNE/log_Size.csv")

###########################################
# Convert Categorical to Numerical
########################################### 
#Label Encoding: convert categorical to numerical
label_encoder = preprocessing.LabelEncoder()
df['chrom'] = label_encoder.fit_transform(df['chrom'])
df['SVtype'] = label_encoder.fit_transform(df['SVtype'])
df['sample'] = label_encoder.fit_transform(df['sample'])
df['type'] = label_encoder.fit_transform(df['type'])
# Count Number of NaN in each column
dfNaN = pd.DataFrame()
NaN_count_pre = df.isnull().sum()
dfNaN['pre'] = NaN_count_pre

###########################################
# KNN to impute missing value
########################################### 

#Convert dataframe to matrix
X = df.as_matrix()

# Imput missing values from three closest observations
X_imputed = KNN(k=3).complete(X)
df2 = pd.DataFrame(X_imputed)

#Re-label all columns in the dataframe
df2.columns = ['chrom', 'start', 'end', 'sample', 'id', 'type', 'SVtype', 'Size', 'Ill300x.alt_alnScore_mean', 'Ill300x.alt_alnScore_std', 'Ill300x.alt_count', 'Ill300x.alt_insertSize_mean', 'Ill300x.alt_insertSize_std', 'Ill300x.alt_reason_alignmentScore', 'Ill300x.alt_reason_insertSizeScore', 'Ill300x.alt_reason_orientation', 'Ill300x.amb_alnScore_mean', 'Ill300x.amb_alnScore_std', 'Ill300x.amb_count', 'Ill300x.amb_insertSize_mean', 'Ill300x.amb_insertSize_std', 'Ill300x.amb_reason_alignmentScore_alignmentScore', 'Ill300x.amb_reason_alignmentScore_insertSizeScore', 'Ill300x.amb_reason_alignmentScore_orientation', 'Ill300x.amb_reason_flanking', 'Ill300x.amb_reason_insertSizeScore_insertSizeScore', 'Ill300x.amb_reason_insertSizeScore_orientation', 'Ill300x.amb_reason_multimapping', 'Ill300x.amb_reason_orientation_alignmentScore', 'Ill300x.amb_reason_orientation_orientation', 'Ill300x.amb_reason_same_scores', 'Ill300x.ref_alnScore_mean', 'Ill300x.ref_alnScore_std', 'Ill300x.ref_count', 'Ill300x.ref_insertSize_mean', 'Ill300x.ref_insertSize_std', 'Ill300x.ref_reason_alignmentScore', 'Ill300x.ref_reason_insertSizeScore', 'Ill300x.ref_reason_orientation', 'Ill300x.GT', 'Ill250.alt_alnScore_mean', 'Ill250.alt_alnScore_std', 'Ill250.alt_count', 'Ill250.alt_insertSize_mean', 'Ill250.alt_insertSize_std', 'Ill250.alt_reason_alignmentScore', 'Ill250.alt_reason_insertSizeScore', 'Ill250.alt_reason_orientation', 'Ill250.amb_alnScore_mean', 'Ill250.amb_alnScore_std', 'Ill250.amb_count', 'Ill250.amb_insertSize_mean', 'Ill250.amb_insertSize_std', 'Ill250.amb_reason_alignmentScore_alignmentScore', 'Ill250.amb_reason_alignmentScore_orientation', 'Ill250.amb_reason_flanking', 'Ill250.amb_reason_insertSizeScore_insertSizeScore', 'Ill250.amb_reason_multimapping', 'Ill250.amb_reason_orientation_alignmentScore', 'Ill250.amb_reason_orientation_orientation', 'Ill250.amb_reason_same_scores', 'Ill250.ref_alnScore_mean', 'Ill250.ref_alnScore_std', 'Ill250.ref_count', 'Ill250.ref_insertSize_mean', 'Ill250.ref_insertSize_std', 'Ill250.ref_reason_alignmentScore', 'Ill250.ref_reason_insertSizeScore', 'Ill250.ref_reason_orientation', 'Ill250.GT', 'IllMP.alt_alnScore_mean', 'IllMP.alt_alnScore_std', 'IllMP.alt_count', 'IllMP.alt_insertSize_mean', 'IllMP.alt_insertSize_std', 'IllMP.alt_reason_alignmentScore', 'IllMP.alt_reason_insertSizeScore', 'IllMP.alt_reason_orientation', 'IllMP.amb_alnScore_mean', 'IllMP.amb_alnScore_std', 'IllMP.amb_count', 'IllMP.amb_insertSize_mean', 'IllMP.amb_insertSize_std', 'IllMP.amb_reason_alignmentScore_alignmentScore', 'IllMP.amb_reason_alignmentScore_orientation', 'IllMP.amb_reason_flanking', 'IllMP.amb_reason_insertSizeScore_insertSizeScore', 'IllMP.amb_reason_multimapping', 'IllMP.amb_reason_orientation_alignmentScore', 'IllMP.amb_reason_orientation_orientation', 'IllMP.amb_reason_same_scores', 'IllMP.ref_alnScore_mean', 'IllMP.ref_alnScore_std', 'IllMP.ref_count', 'IllMP.ref_insertSize_mean', 'IllMP.ref_insertSize_std', 'IllMP.ref_reason_alignmentScore', 'IllMP.ref_reason_insertSizeScore', 'IllMP.ref_reason_orientation', 'IllMP.GT', 'TenX.HP1_alt_alnScore_mean', 'TenX.HP1_alt_alnScore_std', 'TenX.HP1_alt_count', 'TenX.HP1_alt_insertSize_mean', 'TenX.HP1_alt_insertSize_std', 'TenX.HP1_alt_reason_alignmentScore', 'TenX.HP1_alt_reason_insertSizeScore', 'TenX.HP1_alt_reason_orientation', 'TenX.HP1_amb_alnScore_mean', 'TenX.HP1_amb_alnScore_std', 'TenX.HP1_amb_count', 'TenX.HP1_amb_insertSize_mean', 'TenX.HP1_amb_insertSize_std', 'TenX.HP1_amb_reason_alignmentScore_alignmentScore', 'TenX.HP1_amb_reason_alignmentScore_orientation', 'TenX.HP1_amb_reason_flanking', 'TenX.HP1_amb_reason_insertSizeScore_insertSizeScore', 'TenX.HP1_amb_reason_multimapping', 'TenX.HP1_amb_reason_orientation_alignmentScore', 'TenX.HP1_amb_reason_orientation_orientation', 'TenX.HP1_amb_reason_same_scores', 'TenX.HP1_ref_alnScore_mean', 'TenX.HP1_ref_alnScore_std', 'TenX.HP1_ref_count', 'TenX.HP1_ref_insertSize_mean', 'TenX.HP1_ref_insertSize_std', 'TenX.HP1_ref_reason_alignmentScore', 'TenX.HP1_ref_reason_insertSizeScore', 'TenX.HP1_ref_reason_orientation', 'TenX.HP2_alt_alnScore_mean', 'TenX.HP2_alt_alnScore_std', 'TenX.HP2_alt_count', 'TenX.HP2_alt_insertSize_mean', 'TenX.HP2_alt_insertSize_std', 'TenX.HP2_alt_reason_alignmentScore', 'TenX.HP2_alt_reason_insertSizeScore', 'TenX.HP2_alt_reason_orientation', 'TenX.HP2_amb_alnScore_mean', 'TenX.HP2_amb_alnScore_std', 'TenX.HP2_amb_count', 'TenX.HP2_amb_insertSize_mean', 'TenX.HP2_amb_insertSize_std', 'TenX.HP2_amb_reason_alignmentScore_alignmentScore', 'TenX.HP2_amb_reason_alignmentScore_orientation', 'TenX.HP2_amb_reason_flanking', 'TenX.HP2_amb_reason_multimapping', 'TenX.HP2_amb_reason_orientation_alignmentScore', 'TenX.HP2_amb_reason_orientation_insertSizeScore', 'TenX.HP2_amb_reason_orientation_orientation', 'TenX.HP2_amb_reason_same_scores', 'TenX.HP2_ref_alnScore_mean', 'TenX.HP2_ref_alnScore_std', 'TenX.HP2_ref_count', 'TenX.HP2_ref_insertSize_mean', 'TenX.HP2_ref_insertSize_std', 'TenX.HP2_ref_reason_alignmentScore', 'TenX.HP2_ref_reason_insertSizeScore', 'TenX.HP2_ref_reason_orientation', 'TenX.GT', 'pacbio.alt_alnScore_mean', 'pacbio.alt_alnScore_std', 'pacbio.alt_count', 'pacbio.alt_insertSize_mean', 'pacbio.alt_insertSize_std', 'pacbio.alt_reason_alignmentScore', 'pacbio.amb_alnScore_mean', 'pacbio.amb_alnScore_std', 'pacbio.amb_count', 'pacbio.amb_insertSize_mean', 'pacbio.amb_insertSize_std', 'pacbio.amb_reason_alignmentScore_alignmentScore', 'pacbio.amb_reason_flanking', 'pacbio.amb_reason_multimapping', 'pacbio.amb_reason_same_scores', 'pacbio.ref_alnScore_mean', 'pacbio.ref_alnScore_std', 'pacbio.ref_count', 'pacbio.ref_insertSize_mean', 'pacbio.ref_insertSize_std', 'pacbio.ref_reason_alignmentScore', 'pacbio.GT', 'GTcons', 'GTconflict', 'GTsupp', 'tandemrep_cnt', 'tandemrep_pct', 'segdup_cnt', 'segdup_pct', 'refN_cnt', 'refN_pct']
df2.drop('GTcons',axis=1)
# df2.drop('Ill300x.GT',axis=1)
# df2.drop('pacbio.GT',axis=1)
# df2.drop('Ill250.GT',axis=1)
# df2.drop('IllMP.GT',axis=1)
# df2.drop('TenX.GT',axis=1)

# Count NaNs post KNN imputation
NaN_count_post = df2.isnull().sum()
dfNaN['post'] = NaN_count_post

# Scaled Data
# Standardize features by removing the mean and scaling to unit variance
scaler = preprocessing.StandardScaler()
X = scaler.fit_transform(df2)

###########################################
# SVD
########################################### 
ncomps = 100
svd = TruncatedSVD(n_components=ncomps)
svd_fit = svd.fit(X)
Y = svd.fit_transform(X)
dfsvd = pd.DataFrame(Y, columns=['c{}'.format(c) for c in range(ncomps)], index=df.index)

###########################################
# MDS
########################################### 

dfMDS = pd.DataFrame(X)
clf = manifold.MDS(n_components=2, max_iter=100, n_init=1)
X_mds = clf.fit_transform(dfsvd)
dfMDS = pd.DataFrame(X_mds, columns=['x','y'], index=dfMDS.index)

dfMDS['GTcons'] = df4['GTcons']
ax = sns.lmplot('x', 'y', dfMDS, hue='GTcons', fit_reg=False, size=8, scatter_kws={'alpha':0.7,'s':60})
# plt.savefig("/Volumes/lesleydata/SVVIZOutput/April112017/Step4/MachineLearning/Figures/tSNE.test/DEL/MDS_SVD_DEL.png")

###########################################
# PCA/MDS
########################################### 
'''
Do not use data
'''
sklearn_pca = sklearnPCA(n_components=2)
Y_sklearn = sklearn_pca.fit_transform(dfMDS)
yCol = df4['GTcons']
plt.scatter(Y_sklearn[:,0], Y_sklearn[:,1], c=yCol, edgecolor='none', alpha=0.5)
mds = manifold.MDS(n_components=2, max_iter=100, n_init=1)
Y = mds.fit_transform(X)


###########################################
# TSNE
########################################### 
tsne = TSNE(n_components=2, random_state=0)
Z = tsne.fit_transform(dfsvd)
dftsne = pd.DataFrame(Z, columns=['x','y'], index=dfsvd.index)
print dftsne.shape

###########################################
# DBSCAN
########################################### 
# DBSCAN with tSNE data
dbscan = DBSCAN()
labels = dbscan.fit_predict(Z)
print("Unique labels: {}".format(np.unique(labels)))
df['clusterLabel'] = labels
df.to_csv('INS.tSNE.csv', index=False)

# DBSCAN with SVD data
dbscan = DBSCAN()
labels = dbscan.fit_predict(Y)
print("Unique labels: {}".format(np.unique(labels)))
df['clusterLabel.SVD'] = labels
df.to_csv('INS.tSNE.SVD.csv', index=False)

# DBSCAN with raw data
dbscan = DBSCAN()
labels = dbscan.fit_predict(X)
print("Unique labels: {}".format(np.unique(labels)))
df['clusterLabel.raw'] = labels
df.to_csv('INS.tSNE.raw.csv', index=False)


###########################################
# Plots
########################################### 

'''
Data Cleaning
'''
dftsne['tandemrep_pct'] = df4['tandemrep_pct']
dftsne['segdup_pct'] = df4['segdup_pct']
dftsne['segdup_pct'].replace(0,-1,inplace=True)
dftsne['tandemrep_pct'].replace(0,-1,inplace=True)

bins = [-1, 0.2, 0.5, 1]
group_names = ['0-0.2', '0.2-0.5', '0.5-1']
df4['cat'] = pd.cut(df4['segdup_pct'], bins, labels=group_names)
df4['cat2'] = pd.cut(df4['tandemrep_pct'], bins, labels=group_names)

#Size Bins
bins = [20,50,100,1000,3000,9062]
df4['Size'] = df4['Size'].abs()
group_names_size = ['20-50', '50-100', '100-1000', '1000-3000', '3000-9062']
df4['size_bin'] = pd.cut(df4['Size'], bins, labels=group_names_size)
dftsne['cat'] = df4['cat']
dftsne['cat2'] = df4['cat2']
dftsne['size_bin'] = df4['size_bin']


df4['Size2'] = df4['Size'].apply(lambda x: x/1000)
dftsne['Size2'] = df4['Size2']
dftsne['Size'] = df4['Size']
dftsne['GTcons'] = df4['GTcons']
dftsne['sample'] = df4['sample']
dftsne['refN_pct'] = df4['refN_pct']
dftsne['label'] = df['clusterLabel']
dftsne['label.SVD'] = df['clusterLabel.SVD']
dftsne['label.raw'] = df['clusterLabel.raw']



# dftsne['cat2'].replace(to_replace=0, value=-1, inplace=True)
# dftsne['cat'].replace(to_replace=0, value=-1, inplace=True)
# df[df != 0] = value
dftsne.to_csv('dftsne.csv', index=False)

'''
Generate plots
'''

p = Scatter(dftsne, x='x', y='y', title='HG002 INS: tSNE')
output_file("tSNE1_INS.html")
show(p)

p = Scatter(dftsne, x='x', y='y', color='cat2', title='HG002 INS: tSNE tandem repeats', legend="top_left")
output_file("tSNE2_INS_tandRep.html")
show(p)

p = Scatter(dftsne, x='x', y='y', color='label', title='HG002 INS: tSNE DBSCAN labels', legend="top_left")
output_file("tSNE2_DBSCAN_label.html")
show(p)

p = Scatter(dftsne, x='x', y='y', color='label.SVD', title='HG002 INS: SVD DBSCAN labels', legend="top_left")
output_file("SVD_DBSCAN_label.html")
show(p)

p = Scatter(dftsne, x='x', y='y', color='label.raw', title='HG002 INS: Raw DBSCAN labels', legend="top_left")
output_file("raw_DBSCAN_label.html")
show(p)

p = Scatter(dftsne, x='x', y='y', color='cat', title='HG002 INS: tSNE segmental duplications', legend="top_left")
output_file("tSNE3_INS_segDup.html")
show(p)

p = Histogram(log_size, values='INS_log_size', title='HG002 INS: Size Distribution [5000 Samples]', color='LightSlateGray', bins=19, xlabel="Size[log10]", ylabel="Frequency")
output_file("tSNE4_INS_Histo_logsize.html")
show(p)

p = Histogram(log_size, values='INS_log_size', title='HG002 INS: Size Distribution [5000 Samples]', color='LightSlateGray', bins=30, xlabel="Size[log10]", ylabel="Frequency")
output_file("tSNE4_INS_Histo_logsize.2.html")
show(p)

p = Scatter(dftsne, x='x', y='y', color='GTcons', title='HG002 INS: Consensus Genotypes', legend="top_left")
output_file("tSNE6_INS_GTcons.html")
show(p)

p = Scatter(dftsne, x='x', y='y', color='refN_pct', title='HG002 INS: Reference N', legend="top_left")
output_file("tSNE7_INS_RefN.html")
show(p)

p = Scatter(dftsne, x='x', y='y', color='size_bin', title='HG002 INS:Size', legend="top_left")
output_file("tSNE7_INS_SizeBin.html")
show(p)
