import pandas as pd


df = pd.read_csv('/Users/lmc2/X2X6_columns.csv')
df1 = pd.DataFrame()
df2 = pd.DataFrame()

df1['lab'] = df['X2']
df2['lab'] = df['X6']

find = ~df2['lab'].isin(df1['lab']) & df1['lab'].isin(df2['lab'])

df3 = pd.DataFrame()
df3 = df1[find].append(df2[find])
print df3