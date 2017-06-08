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
from ggplot import *
# from .theme import theme
# from .theme import theme_matplotlib
# from .theme_matplotlib import theme_matplotlib
from sklearn import (manifold, datasets, decomposition, ensemble,
                     discriminant_analysis, random_projection)



df = pd.read_csv("/Volumes/lesleydata/SVVIZOutput/April112017/Step4/MachineLearning/Step1.DataCleaning.Output/DEL/svviz.Annotate.DEL.HG002.csv")
df4 = pd.read_csv("/Volumes/lesleydata/SVVIZOutput/April112017/Step4/MachineLearning/Step1.DataCleaning.Output/DEL/svviz.Annotate.DEL.HG002.csv")


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
df2.columns = ['chrom', 'start', 'end', 'sample', 'id', 'type', 'SVtype', 'Size', 'Ill300x.alt_alnScore_mean', 'Ill300x.alt_alnScore_std', 'Ill300x.alt_count', 'Ill300x.alt_insertSize_mean', 'Ill300x.alt_insertSize_std', 'Ill300x.alt_reason_alignmentScore', 'Ill300x.alt_reason_insertSizeScore', 'Ill300x.alt_reason_orientation', 'Ill300x.amb_alnScore_mean', 'Ill300x.amb_alnScore_std', 'Ill300x.amb_count', 'Ill300x.amb_insertSize_mean', 'Ill300x.amb_insertSize_std', 'Ill300x.amb_reason_alignmentScore_alignmentScore', 'Ill300x.amb_reason_alignmentScore_orientation', 'Ill300x.amb_reason_flanking', 'Ill300x.amb_reason_insertSizeScore_alignmentScore', 'Ill300x.amb_reason_insertSizeScore_insertSizeScore', 'Ill300x.amb_reason_insertSizeScore_orientation', 'Ill300x.amb_reason_multimapping', 'Ill300x.amb_reason_orientation_alignmentScore', 'Ill300x.amb_reason_orientation_orientation', 'Ill300x.amb_reason_same_scores', 'Ill300x.ref_alnScore_mean', 'Ill300x.ref_alnScore_std', 'Ill300x.ref_count', 'Ill300x.ref_insertSize_mean', 'Ill300x.ref_insertSize_std', 'Ill300x.ref_reason_alignmentScore', 'Ill300x.ref_reason_insertSizeScore', 'Ill300x.ref_reason_orientation', 'Ill300x.GT', 'Ill250.alt_alnScore_mean', 'Ill250.alt_alnScore_std', 'Ill250.alt_count', 'Ill250.alt_insertSize_mean', 'Ill250.alt_insertSize_std', 'Ill250.alt_reason_alignmentScore', 'Ill250.alt_reason_insertSizeScore', 'Ill250.alt_reason_orientation', 'Ill250.amb_alnScore_mean', 'Ill250.amb_alnScore_std', 'Ill250.amb_count', 'Ill250.amb_insertSize_mean', 'Ill250.amb_insertSize_std', 'Ill250.amb_reason_alignmentScore_alignmentScore', 'Ill250.amb_reason_alignmentScore_orientation', 'Ill250.amb_reason_flanking', 'Ill250.amb_reason_insertSizeScore_alignmentScore', 'Ill250.amb_reason_multimapping', 'Ill250.amb_reason_orientation_alignmentScore', 'Ill250.amb_reason_orientation_orientation', 'Ill250.amb_reason_same_scores', 'Ill250.ref_alnScore_mean', 'Ill250.ref_alnScore_std', 'Ill250.ref_count', 'Ill250.ref_insertSize_mean', 'Ill250.ref_insertSize_std', 'Ill250.ref_reason_alignmentScore', 'Ill250.ref_reason_orientation', 'Ill250.GT', 'IllMP.alt_alnScore_mean', 'IllMP.alt_alnScore_std', 'IllMP.alt_count', 'IllMP.alt_insertSize_mean', 'IllMP.alt_insertSize_std', 'IllMP.alt_reason_alignmentScore', 'IllMP.alt_reason_insertSizeScore', 'IllMP.alt_reason_orientation', 'IllMP.amb_alnScore_mean', 'IllMP.amb_alnScore_std', 'IllMP.amb_count', 'IllMP.amb_insertSize_mean', 'IllMP.amb_insertSize_std', 'IllMP.amb_reason_alignmentScore_alignmentScore', 'IllMP.amb_reason_alignmentScore_orientation', 'IllMP.amb_reason_flanking', 'IllMP.amb_reason_insertSizeScore_alignmentScore', 'IllMP.amb_reason_insertSizeScore_insertSizeScore', 'IllMP.amb_reason_multimapping', 'IllMP.amb_reason_orientation_alignmentScore', 'IllMP.amb_reason_orientation_orientation', 'IllMP.amb_reason_same_scores', 'IllMP.ref_alnScore_mean', 'IllMP.ref_alnScore_std', 'IllMP.ref_count', 'IllMP.ref_insertSize_mean', 'IllMP.ref_insertSize_std', 'IllMP.ref_reason_alignmentScore', 'IllMP.ref_reason_insertSizeScore', 'IllMP.ref_reason_orientation', 'IllMP.GT', 'TenX.HP1_alt_alnScore_mean', 'TenX.HP1_alt_alnScore_std', 'TenX.HP1_alt_count', 'TenX.HP1_alt_insertSize_mean', 'TenX.HP1_alt_insertSize_std', 'TenX.HP1_alt_reason_alignmentScore', 'TenX.HP1_alt_reason_insertSizeScore', 'TenX.HP1_alt_reason_orientation', 'TenX.HP1_amb_alnScore_mean', 'TenX.HP1_amb_alnScore_std', 'TenX.HP1_amb_count', 'TenX.HP1_amb_insertSize_mean', 'TenX.HP1_amb_insertSize_std', 'TenX.HP1_amb_reason_alignmentScore_alignmentScore', 'TenX.HP1_amb_reason_alignmentScore_orientation', 'TenX.HP1_amb_reason_flanking', 'TenX.HP1_amb_reason_insertSizeScore_alignmentScore', 'TenX.HP1_amb_reason_insertSizeScore_insertSizeScore', 'TenX.HP1_amb_reason_multimapping', 'TenX.HP1_amb_reason_orientation_alignmentScore', 'TenX.HP1_amb_reason_orientation_orientation', 'TenX.HP1_amb_reason_same_scores', 'TenX.HP1_ref_alnScore_mean', 'TenX.HP1_ref_alnScore_std', 'TenX.HP1_ref_count', 'TenX.HP1_ref_insertSize_mean', 'TenX.HP1_ref_insertSize_std', 'TenX.HP1_ref_reason_alignmentScore', 'TenX.HP1_ref_reason_insertSizeScore', 'TenX.HP1_ref_reason_orientation', 'TenX.HP2_alt_alnScore_mean', 'TenX.HP2_alt_alnScore_std', 'TenX.HP2_alt_count', 'TenX.HP2_alt_insertSize_mean', 'TenX.HP2_alt_insertSize_std', 'TenX.HP2_alt_reason_alignmentScore', 'TenX.HP2_alt_reason_insertSizeScore', 'TenX.HP2_alt_reason_orientation', 'TenX.HP2_amb_alnScore_mean', 'TenX.HP2_amb_alnScore_std', 'TenX.HP2_amb_count', 'TenX.HP2_amb_insertSize_mean', 'TenX.HP2_amb_insertSize_std', 'TenX.HP2_amb_reason_alignmentScore_alignmentScore', 'TenX.HP2_amb_reason_alignmentScore_orientation', 'TenX.HP2_amb_reason_flanking', 'TenX.HP2_amb_reason_insertSizeScore_alignmentScore', 'TenX.HP2_amb_reason_insertSizeScore_insertSizeScore', 'TenX.HP2_amb_reason_multimapping', 'TenX.HP2_amb_reason_orientation_alignmentScore', 'TenX.HP2_amb_reason_orientation_insertSizeScore', 'TenX.HP2_amb_reason_orientation_orientation', 'TenX.HP2_amb_reason_same_scores', 'TenX.HP2_ref_alnScore_mean', 'TenX.HP2_ref_alnScore_std', 'TenX.HP2_ref_count', 'TenX.HP2_ref_insertSize_mean', 'TenX.HP2_ref_insertSize_std', 'TenX.HP2_ref_reason_alignmentScore', 'TenX.HP2_ref_reason_orientation', 'TenX.GT', 'pacbio.alt_alnScore_mean', 'pacbio.alt_alnScore_std', 'pacbio.alt_count', 'pacbio.alt_insertSize_mean', 'pacbio.alt_insertSize_std', 'pacbio.alt_reason_alignmentScore', 'pacbio.amb_alnScore_mean', 'pacbio.amb_alnScore_std', 'pacbio.amb_count', 'pacbio.amb_insertSize_mean', 'pacbio.amb_insertSize_std', 'pacbio.amb_reason_alignmentScore_alignmentScore', 'pacbio.amb_reason_flanking', 'pacbio.amb_reason_multimapping', 'pacbio.amb_reason_same_scores', 'pacbio.ref_alnScore_mean', 'pacbio.ref_alnScore_std', 'pacbio.ref_count', 'pacbio.ref_insertSize_mean', 'pacbio.ref_insertSize_std', 'pacbio.ref_reason_alignmentScore', 'pacbio.GT', 'GTcons', 'GTconflict', 'GTsupp', 'tandemrep_cnt', 'tandemrep_pct', 'segdup_cnt', 'segdup_pct', 'refN_cnt', 'refN_pct']

# Count NaNs post KNN imputation
NaN_count_post = df2.isnull().sum()
dfNaN['post'] = NaN_count_post

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
# Plots
########################################### 

dftsne['tandemrep_pct'] = df4['tandemrep_pct']
dftsne['segdup_pct'] = df4['segdup_pct']
dftsne['segdup_pct'].replace(0,-1,inplace=True)
dftsne['tandemrep_pct'].replace(0,-1,inplace=True)

bins = [-1, 0.2, 0.5, 1]
group_names = ['Low', 'Medium', 'High']

df4['cat'] = pd.cut(df4['segdup_pct'], bins, labels=group_names)
df4['cat2'] = pd.cut(df4['tandemrep_pct'], bins, labels=group_names)
dftsne['cat'] = df4['cat']
dftsne['cat2'] = df4['cat2']
# dftsne['cat2'].replace(to_replace=0, value=-1, inplace=True)
# dftsne['cat'].replace(to_replace=0, value=-1, inplace=True)
# df[df != 0] = value
dftsne.to_csv('dftsne.csv', index=False)

ggplot(aesthetics=aes(x='x', y='y'), data=dftsne)

df4['Size2'] = df4['Size'].apply(lambda x: x/1000)
my_plot = ggplot(df4, aes(x='Size2')) + geom_histogram() + xlab('Size[kb]') + ylab('Frequency')
my_plot.save("name_of_file4.png", width=15, height=10)

my_plot = ggplot(aes(x = 'x', y = 'y', color='tandemrep_pct'),data = dftsne) + geom_point(alpha = 0.1) + scale_color_gradient(low='yellow', high='red')
my_plot.save("name_of_file2.png", width=15, height=10)

# my_plot = ggplot(aes(x = 'x', y = 'y', color='cat', shape='cat'),data = dftsne) + geom_point(alpha = 0.1) + scale_color_brewer() + theme_matplotlib()
# my_plot.save("name_of_file6.png", width=15, height=10)

my_plot = ggplot(aes(x = 'x', y = 'y', color='cat2'),data = dftsne) + geom_point(alpha = 0.1) + scale_color_brewer(type='qual', palette=2) 
my_plot.save("name_of_file20.png", width=15, height=10)

my_plot = ggplot(aes(x = 'x', y = 'y', color='cat', shape='cat'),data = dftsne) + geom_point(alpha = 0.1) + scale_color_brewer(type='qual', palette=2) 
my_plot.save("name_of_file60.png", width=15, height=10)

my_plot = ggplot(aes(x = 'x', y = 'y', color='cat2'),data = dftsne) + geom_point(alpha = 0.1) + scale_color_brewer(type='qual', palette=2) 
my_plot.save("name_of_file200.png", width=15, height=10)

my_plot = ggplot(aes(x = 'x', y = 'y', color='cat', shape='cat'),data = dftsne) + geom_point(alpha = 0.1) + scale_color_brewer(type='qual', palette=2) 
my_plot.save("name_of_file600.png", width=15, height=10)

df4['Size'] = df4['Size'].abs()
# my_plot = ggplot(df4, aes(x='Size')) + geom_histogram()
# my_plot.save("name_of_file3.png", width=15, height=10)

df4['Size2'] = df4['Size'].apply(lambda x: x/1000)
my_plot = ggplot(df4, aes(x='Size2')) + geom_histogram() + ylab('Frequency')
my_plot.save("name_of_file4.png", width=15, height=10)

# my_plot = ggplot(aes(x = 'x', y = 'y', color='tandemrep_pct'),data = dftsne) + geom_point(alpha = 0.1) + facet_wrap('cat2')
# my_plot.save("name_of_file5.png", width=15, height=10)
