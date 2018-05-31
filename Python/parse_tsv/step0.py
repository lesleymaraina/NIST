import os
import pandas as pd

#list the files
path  = '/Users/lmc2/Downloads/svvizgenosvIll150bp_1/tsv_files'
filelist = os.listdir(path) 
print(filelist)
#read them into pandas
df_list = [pd.read_table(file) for file in filelist]
#concatenate them together
all_df = pd.concat(df_list)
print (all_df.head(3))