####################################
# Date: May 21 2018

# Resource : https://stackoverflow.com/questions/25009214/reshaping-data-frame-containing-non-numeric-value-using-pandas
# Overall Goal: Pivot final tsv table to reflect final ML df
'''
NOTES
-----
Pivot table on non-numerical values
'''
####################################


#####################################
# Imports
#####################################

import pandas as pd
import glob
import numpy as np
#####################################


###################################################
# Code
###################################################


df = pd.read_table('/Volumes/lesleydata/manual_Curation_app/machine_learning/code/parse_tsv/all_tsv_2.tsv')
df['allele'] = df['allele'].replace(np.nan, '', regex=True)
df['combined'] = df['allele'].astype(str)+'_'+df['key'].astype(str)
df2 = df.pivot_table(index=['filename', 'sample'],columns='combined',values='value', aggfunc=lambda x:  ', '.join(x))
df2.to_csv('/Volumes/lesleydata/manual_Curation_app/machine_learning/code/parse_tsv/final_csv.csv', index=True)
