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

        # print (df2.head(1))
        if index == 0:
            df2.to_csv('all.csv', index=True)
        else:
            df2.to_csv('tmp.csv', index=True)
            content = ""
            with open("tmp.csv", "r") as tmp_rd:
                content = "\n".join(tmp_rd.read().split("\n")[1:])
            with open("all.csv", "a") as all_rd:
                all_rd.write(content)
        index += 1

if __name__ == '__main__':
	# We loop over all the files .tsv and convert each.
    dump_csv("tsv_files/*.tsv")