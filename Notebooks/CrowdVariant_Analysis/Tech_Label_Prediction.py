from bokeh.charts import Scatter, Histogram, output_file, show
from bokeh.io import output_notebook
import bokeh.palettes as palettes
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from fancyimpute import KNN
from matplotlib import pyplot
from sklearn.manifold import TSNE
from sklearn.cluster import DBSCAN
from bokeh.plotting import figure, show
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.decomposition import TruncatedSVD
from bokeh.models import Legend
from bokeh.models import HoverTool, BoxSelectTool
from bokeh.plotting import figure, output_file, show, ColumnDataSource
# Import Bokeh modules for interactive plotting
import bokeh.charts
import bokeh.charts as bch
import bokeh.charts.utils
import bokeh.io
import bokeh.models
import bokeh.palettes
import bokeh.plotting

# Display graphics in this notebook
output_notebook()


#Load Data and Data Cleaning
df_all = pd.read_csv('/Users/lmc2/NIST/Notebooks/CrowdVariant_Analysis/All_Technologies.csv')
df_10X = pd.read_csv('/Users/lmc2/NIST/Notebooks/CrowdVariant_Analysis/10X_pred_prob.csv')
df_MP = pd.read_csv('/Users/lmc2/NIST/Notebooks/CrowdVariant_Analysis/MP_pred_prob.csv')
df_250bp = pd.read_csv('/Users/lmc2/NIST/Notebooks/CrowdVariant_Analysis/250bp_pred_prob.csv')
df_300X = pd.read_csv('/Users/lmc2/NIST/Notebooks/CrowdVariant_Analysis/300x_pred_prob.csv')
df_PB = pd.read_csv('/Users/lmc2/NIST/Notebooks/CrowdVariant_Analysis/PB_pred_prob.csv')

df_all['chrom'].replace('X', 23, inplace=True)
df_all['chrom'].replace('Y', 24, inplace=True)

df_10X_2 = df_10X[['chrom','start','end', '10X_predicted_label']]
df_MP_2 = df_MP[['chrom','start','end', 'MP_predicted_label']]
df_250bp_2 = df_250bp[['chrom','start','end', '250bp_predicted_label']]
df_300X_2 = df_300X[['chrom','start','end', '300x_predicted_label']]
df_PB_2 = df_PB[['chrom','start','end', 'PB_predicted_label']]

df_10X_3 = df_10X_2.drop_duplicates()
df_MP_3 = df_MP_2.drop_duplicates()
df_250bp_3 = df_250bp_2.drop_duplicates()
df_300X_3 = df_300X_2.drop_duplicates()
df_PB_3 = df_PB_2.drop_duplicates()

df_10X_MP2 = pd.DataFrame()
df_10X_MP2 = pd.merge(df_10X_3, df_MP_3, on=['chrom', 'start', 'end'], how='left')
df3 = pd.DataFrame()
df3 = pd.merge(df_10X_MP2, df_250bp_3, on=['chrom', 'start', 'end'], how='left')
df4 = pd.DataFrame()
df4 = pd.merge(df3, df_300X_3, on=['chrom', 'start', 'end'], how='left')
df5 = pd.DataFrame()
df5 = pd.merge(df4, df_PB_3, on=['chrom', 'start', 'end'], how='left')
df5['total'] = df5['10X_predicted_label'] + df5['MP_predicted_label'] + df5['250bp_predicted_label'] + df5['300x_predicted_label'] + df5['PB_predicted_label']
df6 = pd.DataFrame()
df6 = pd.merge(df4, df_PB_3, on=['chrom', 'start', 'end'], how='left')
df6 = df6.dropna()

# Copy dataframe to keep column values
df6_2 = pd.DataFrame()
df6_2 = pd.merge(df4, df_PB_3, on=['chrom', 'start', 'end'], how='left')
df6_2 = df6_2.dropna()
df6.drop(['chrom'], axis=1, inplace = True)
df6.drop(['start'], axis=1, inplace = True)
df6.drop(['end'], axis=1, inplace = True)
df6 = df6.astype(str)
df6['1'] = df6.apply(lambda s: (s == '1.0').sum(), axis=1)
df6['2'] = df6.apply(lambda s: (s == '2.0').sum(), axis=1)
df6['0'] = df6.apply(lambda s: (s == '0.0').sum(), axis=1)
df6 = df6.astype(float)
df6['max_col_name'] = df6.idxmax(axis=1)
df7 = pd.DataFrame()
df7 = df6[['1','2','0']]
df7['max_value'] = df7.max(axis=1)

df7['min_value'] = df7.min(axis=1)
df6['max_value'] = df7['max_value']
df6['min_value'] = df7['min_value']
df6['chrom'] = df6_2['chrom']
df6['start'] = df6_2['start']
df6['end'] = df6_2['end']
df_all_3 = df_all.drop_duplicates()

df_all_4 = pd.read_csv('/Users/lmc2/NIST/Notebooks/Bokeh.Tests/df_all_4_2.csv')
# FYI: Parsed values above computed in the: Technology_Label_Prediction.ipynb
# df_all_4 = pd.merge(df_all_3, df6, on=['chrom', 'start', 'end'], how='left')

df_all_5 = pd.read_csv('/Users/lmc2/NIST/Notebooks/Bokeh.Tests/df_all_4_2.csv')
# df_all_5 = pd.merge(df_all_3, df6, on=['chrom', 'start', 'end'], how='left')

df_all_5.drop(['10X_predicted_label'], axis=1, inplace = True)
df_all_5.drop(['MP_predicted_label'], axis=1, inplace = True)
df_all_5.drop(['250bp_predicted_label'], axis=1, inplace = True)
df_all_5.drop(['300x_predicted_label'],axis=1, inplace = True)
df_all_5.drop(['1'],axis=1, inplace = True)
df_all_5.drop(['2'],axis=1, inplace = True)
df_all_5.drop(['0'],axis=1, inplace = True)
df_all_5.drop(['max_col_name'],axis=1, inplace = True)
df_all_5.drop(['max_value'],axis=1, inplace = True)
df_all_5.drop(['min_value'],axis=1, inplace = True)


####################################################
# Data Analysis
####################################################

#Impute Missing Values
X2 = df_all_5
#Convert dataframe to matrix
X2=X2.as_matrix()

#Imput missing values from three closest observations
X2_imputed=KNN(k=3).complete(X2)
X2=pd.DataFrame(X2_imputed)
df_all_5_header = list(df_all_5.columns.values)
X2.columns = df_all_5_header

#Scale Data
#Standardizefeaturesbyremovingthemeanandscalingtounitvariance
scaler=preprocessing.StandardScaler()
X=scaler.fit_transform(X2)


#tSNE Analysis
# 1. SVD Decomposition - will make tSNE run faster

###########################################
#SVD
###########################################
ncomps=100
svd=TruncatedSVD(n_components=ncomps)
svd_fit=svd.fit(X)
Y=svd.fit_transform(X)
dfsvd = pd.DataFrame(Y, columns=['c{}'.format(c) for c in range(ncomps)], index=df_all_5.index)
###########################################
# TSNE
########################################### 
tsne = TSNE(n_components=2, random_state=0)
Z = tsne.fit_transform(dfsvd)
dftsne = pd.DataFrame(Z, columns=['x','y'], index=dfsvd.index)
dftsne.shape
dftsne['Tech_Label_Agreement'] = df_all_4['max_value']
dftsne['GTcons'] = df_MP['GTcons']
dftsne['Tech_minLabel_Agreement'] = df_all_4['min_value']
dftsne['Tech_Consensus_GT'] = df_all_4['max_col_name']
dftsne['MP_predicted_label'] = df_all_4['MP_predicted_label']
dftsne['250bp_predicted_label'] = df_all_4['250bp_predicted_label']
dftsne['300x_predicted_label'] = df_all_4['300x_predicted_label']
dftsne['PB_predicted_label'] = df_all_4['PB_predicted_label']
dftsne['10X_predicted_label'] = df_all_4['10X_predicted_label']
dftsne['chrom'] = df_all_4['chrom']
dftsne['start'] = df_all_4['start']



# Generate tSNE Plot
#Specify data source
source = bokeh.models.ColumnDataSource(dftsne)
# What pops up on hover?
tooltips = [('Tech_Agreement_Count', '@Tech_Label_Agreement'),
           ('Tech_Consensus_GT', '@Tech_Consensus_GT'),
           ('chrom', '@chrom'),
           ('start', '@start'),
           ('MP_predicted_label', '@MP_predicted_label'),
           ('250bp_predicted_label', '@250bp_predicted_label'),
           ('300x_predicted_label', '@300x_predicted_label'),
           ('PB_predicted_label', '@PB_predicted_label'),
           ('10X_predicted_label', '@10X_predicted_label')]

# Make the hover tool
hover = bokeh.models.HoverTool(tooltips=tooltips)

# Create figure
p = bokeh.plotting.figure(plot_width=650, plot_height=450)

p.xgrid.grid_line_color = 'white'
p.ygrid.grid_line_color = 'white'

# Add the hover tool
p.add_tools(hover)

# Populate glyphs
# p.scatter(x='x', y='y', color='Tech_Label_Agreement', size=7, alpha=0.5, source=source)

# bokeh.io.show(p)

scatter = bch.Scatter(dftsne, x='x', y='y',
                      color='Tech_Label_Agreement',
                      legend="top_right",
                      tooltips=tooltips
                     )
output_file("/Users/lmc2/NIST/Notebooks/CrowdVariant_Analysis/Tech_Label_Prediction_2.html")
bch.show(scatter)

#Specify data source
source = bokeh.models.ColumnDataSource(dftsne)
# What pops up on hover?
tooltips = [('Tech_Agreement_Count', '@Tech_Label_Agreement'),
           ('GTcons', '@GTcons'),
           ('MP_predicted_label', '@MP_predicted_label'),
           ('250bp_predicted_label', '@250bp_predicted_label'),
           ('300x_predicted_label', '@300x_predicted_label'),
           ('PB_predicted_label', '@PB_predicted_label'),
           ('10X_predicted_label', '@10X_predicted_label')]

# Make the hover tool
hover = bokeh.models.HoverTool(tooltips=tooltips)

# Create figure
p = bokeh.plotting.figure(plot_width=650, 
                          plot_height=450)

p.xgrid.grid_line_color = 'white'
p.ygrid.grid_line_color = 'white'

# Add the hover tool
p.add_tools(hover)

# Populate glyphs
# p.scatter(x='x', y='y', color='Tech_Label_Agreement', size=7, alpha=0.5, source=source)

# bokeh.io.show(p)

scatter2 = bch.Scatter(dftsne, x='x', y='y',
                      color='GTcons',
                      legend="top_right",
                      tooltips=tooltips
                     )
output_file("/Users/lmc2/NIST/Notebooks/CrowdVariant_Analysis/Tech_Label_Prediction_GTcons.html")
bch.show(scatter2)



# Generate tSNE Plot
#Specify data source
source = bokeh.models.ColumnDataSource(dftsne)
# What pops up on hover?
tooltips = [('Tech_Agreement_Count', '@Tech_Label_Agreement'),
           ('Tech_Consensus_GT', '@Tech_Consensus_GT'),
           ('chrom', '@chrom'),
           ('start', '@start'),
           ('MP_predicted_label', '@MP_predicted_label'),
           ('250bp_predicted_label', '@250bp_predicted_label'),
           ('300x_predicted_label', '@300x_predicted_label'),
           ('PB_predicted_label', '@PB_predicted_label'),
           ('10X_predicted_label', '@10X_predicted_label')]

# Make the hover tool
hover = bokeh.models.HoverTool(tooltips=tooltips)

# Create figure
p = bokeh.plotting.figure(plot_width=650, plot_height=450)

p.xgrid.grid_line_color = 'white'
p.ygrid.grid_line_color = 'white'

# Add the hover tool
p.add_tools(hover)

# Populate glyphs
# p.scatter(x='x', y='y', color='Tech_Label_Agreement', size=7, alpha=0.5, source=source)

# bokeh.io.show(p)

scatter3 = bch.Scatter(dftsne, x='x', y='y',
                      color='Tech_Consensus_GT',
                      legend="top_right",
                      tooltips=tooltips
                     )
output_file("/Users/lmc2/NIST/Notebooks/CrowdVariant_Analysis/Tech_Label_Prediction_TechGT.html")
bch.show(scatter3)










