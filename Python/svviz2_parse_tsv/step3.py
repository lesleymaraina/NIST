import pandas as pd
import glob

# All the code in a dump function.
# It gets the path to a tsv file.
# Then dumps a csv file in csv_files.
# Filenames is the last word in the tsv name witout the extension.
def dump_csv(path):
    colnames = ['variant',    'sample',    'allele',    'key',    'value']
    index  = 0
    for path in glob.glob(path):
        df = pd.read_table(path)
        # pd.crosstab(index=df['values'], columns=[df['convert_me'], df['age_col']])

        # print (df.head(1))
        df['combined'] = df['allele'].astype(str)+'_'+df['key'].astype(str)
        df2 = df.pivot_table(values='value', index=['variant', 'sample'], columns='combined')