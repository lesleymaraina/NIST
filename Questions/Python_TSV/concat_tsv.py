import pandas as pd
import glob

# All the code in a dump function.
# It gets the path to a tsv file.
# Then dumps a csv file in csv_files.
# Filenames is the last word in the tsv name witout the extension.
def dump_csv(path):
    colnames = ['variant',    'sample',    'allele',    'key',    'value']

    df = pd.read_table(path)
    # pd.crosstab(index=df['values'], columns=[df['convert_me'], df['age_col']])

    # print (df.head(1))
    df['combined'] = df['allele'].astype(str)+'_'+df['key'].astype(str)
    df2 = df.pivot_table(values='value', index=['variant', 'sample'], columns='combined')

    # print (df2.head(1))

    df2.to_csv('csv_files/{0}.csv'.format(path.split("/")[-1].split(".")[-2]), index=True)

if __name__ == '__main__':
	# We loop over all the files .tsv and convert each.
    for path in glob.glob("tsv_files/*.tsv"):
        print("Converting {0}...".format(path))
        dump_csv(path)