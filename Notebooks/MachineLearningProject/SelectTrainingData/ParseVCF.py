###################################################
# Imports 
###################################################
import pandas as pd
import random

###################################################
# Data 
###################################################

# train = pd.read_csv('union_refalt.sort2.txt')
# df = pd.DataFrame(train)
# print df.head(5)
#FYI: How to include names of columns
# colnames = ['A', 'B', 'C', 'D']
# df = pd.read_table('union_refalt.sort2.txt', header=None, names=colnames)


colnames = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
df = pd.read_table('union_refalt.sort.Jan31.3.txt', names=colnames)
# print df.head(5)
# print len(df)

df['H'].fillna('', inplace=True)
dfDel = df[df['H'].str.contains("SVTYPE=DEL")]
dfIns = df[df['H'].str.contains("SVTYPE=INS")]

# print df1.head(5)
# print len(df1)

# print df2.head(5)
# print len(df2)

row = random.sample(dfDel.index, 5000)
df_del = dfDel.ix[row]
df_del_1to1000 = df_del[:1000]
df_del_1001to2000 = df_del[1001:2000]
df_del_2001to3000 = df_del[2001:3000]
df_del_3001to4000 = df_del[3001:4000]
df_del_4001to5000 = df_del[4001:5000]
# print df_del.head(5)
# print len(df_del)
df_del.to_csv('union_refalt.sort.DEL.1to1000.tsv', sep='\t', header=None, index=False)
df_del.to_csv('union_refalt.sort.DEL.1001to2000.tsv', sep='\t', header=None, index=False)
df_del.to_csv('union_refalt.sort.DEL.2001to3000.tsv', sep='\t', header=None, index=False)
df_del.to_csv('union_refalt.sort.DEL.3001to4000.tsv', sep='\t', header=None, index=False)
df_del.to_csv('union_refalt.sort.DEL.4001to5000.tsv', sep='\t', header=None, index=False)

row = random.sample(dfIns.index, 5000)
df_ins = dfIns.ix[row]
df_ins_1to1000 = df_ins[:1000]
df_ins_1001to2000 = df_ins[1001:2000]
df_ins_2001to3000 = df_ins[2001:3000]
df_ins_3001to4000 = df_ins[3001:4000]
df_ins_4001to5000 = df_ins[4001:5000]
# print df_ins.head(5)
# print len(df_ins)
df_ins.to_csv('union_refalt.sort.INS.tsv', sep='\t', header=None, index=False)
df_ins.to_csv('union_refalt.sort.INS.1to1000.tsv', sep='\t', header=None, index=False)
df_ins.to_csv('union_refalt.sort.INS.1001to2000.tsv', sep='\t', header=None, index=False)
df_ins.to_csv('union_refalt.sort.INS.2001to3000.tsv', sep='\t', header=None, index=False)
df_ins.to_csv('union_refalt.sort.INS.3001to4000.tsv', sep='\t', header=None, index=False)
df_ins.to_csv('union_refalt.sort.INS.4001to5000.tsv', sep='\t', header=None, index=False)

# SOURCE: randomly select rows
# http://stackoverflow.com/questions/12190874/pandas-sampling-a-dataframe