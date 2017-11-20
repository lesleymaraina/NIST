import pandas as pd
colnames = ['variant',	'sample',	'allele',	'key',	'value']
df = pd.read_table('/Volumes/LMC/tsv_files/summary_union_refalt.sort.DEL.1to1000_274.tsv')
# pd.crosstab(index=df['values'], columns=[df['convert_me'], df['age_col']])

# print (df.head(1))
df['combined'] = df['allele'].astype(str)+'_'+df['key'].astype(str)
df2 = df.pivot_table(values='value', index=['variant', 'sample'], columns='combined')


print (df2.head(1))

df2.to_csv('df2.csv', index=True)