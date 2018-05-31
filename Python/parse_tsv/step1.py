###################################################
# Imports 
###################################################
import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot
import seaborn as sns
import os
###################################################
# Resources
'''
https://www.quora.com/In-Python-is-there-a-string-function-allows-you-to-remove-characters-from-that-string-and-returns-the-new-string
https://stackoverflow.com/questions/40705480/python-pandas-remove-everything-after-a-delimiter-in-a-string
'''
###################################################


###################################################
# Code
###################################################

'''
Seperate VCF into INS and DEL
'''
# Load Data
colnames = ['sample',	'allele',	'key',	'value']
df = pd.read_csv('/Users/lmc2/Downloads/svvizgenosvIll150bp_1/tsv_files/all_tsv_1.tsv', sep='\t')

sep = 'count_0.alt_part'
sep = 't:'
p = df['key']

df['key_end'] = df['key'].str.rsplit('gion_').str[0]
df['key_end'] = df['key_end'].replace('0.re', '0.region')
df['key_end'] = df['key_end'].replace('1.re', '1.region')
df['key_end'] = df['key_end'].replace('2.re', '2.region')
df['key_end'] = df['key_end'].replace(np.nan, '', regex=True)


m = df['key_end'].str.partition("_part")
first = pd.DataFrame(m)
n = df['key_end'].str.rpartition("_pair")
pair_end = pd.DataFrame(n)
p = df['key_end'].str.rpartition("_seq")
seq_end = pd.DataFrame(p)


df['new_key'] = first[0].astype(str) + first[1].astype(str) + pair_end[1].astype(str) + seq_end[1].astype(str) 
df['n_end'] = df['new_key'].str.rsplit('_n_').str[1]
hg = df['key'].str.rpartition("_n_")

hg2 = pd.DataFrame(hg)
hg2[0] = hg2[0].astype(str).str[0]

df['last_col'] = '###' + hg2[0] + hg2[1] + hg2[2]
df['last_col'] = df['last_col'].replace(np.nan, '', regex=True)
df['final'] = df['new_key'] + df['last_col'] 
hg3 = df['final']
hg4 = pd.DataFrame(hg3)
hg5 = df['final'].str.rpartition("###")

df['final'] = hg5[2]
df = df.drop('key_end', axis=1)
df = df.drop('new_key', axis=1)
df = df.drop('n_end', axis=1)
df = df.drop('last_col', axis=1)
df = df.drop('key', axis=1)
cols = ['filename', 'sample', 'allele', 'final', 'value']
df = df[cols]
df.rename(columns={'final':'key'}, inplace=True)

df['allele'] = df['allele'].replace(np.nan, '', regex=True)
print (df.tail(30))
df.to_csv("all_tsv_2.tsv", sep="\t", index=False)
       














'''
Extra Code
'''
# sep = '...'
# rest = df.key.split(sep, 1)[0]

delimiter = " and "
sentence = "four score and seven"
firstpart, secondpart = sentence.split(delimiter)
revised = firstpart.replace("four", "seven")
charindex = sentence.index("four")
changed = sentence[charindex:] + "days" + sentence[charindex+5:]
# print (sentence)
# print (firstpart)
# print (secondpart)
# print (revised)
# print (charindex) 
# print (changed)



# q = df['key'].str.rpartition("0.region")
# region0 = pd.DataFrame(q)
# r = df['key'].str.rpartition("1.region")
# region1 = pd.DataFrame(r)
# s = df['key'].str.rpartition("2.region")
# region2 = pd.DataFrame(s)
# print (region2.head(30))



# df['n_front'] = df['key'].str.rsplit('_n_').str[0]
# # df['n_front'] = df['n_front'].replace(np.nan, '', regex=True)

# df['n_front_digit'] = df['n_front'].astype(str).str[0]
# # df['n_front_digit'] = df['n_front_digit'].replace(np.nan, '', regex=True)


# df['last_col'] = '###' + df['n_front_digit'] + df['n_end']



# df['key_end'] = df['key_end'].replace('eq', '_seq')
# df['key_end'] = df['key_end'].replace(np.nan, '', regex=True)


#Modify ending characters; prepare to reattach
# df['key_end3'] = df['key'].replace('+_seq171', '+_seq171##')

# df['key_end'] = df['key'].str.rsplit('+_s').str[1]
# df['key_end'] = df['key_end'].replace('eq', '_seq')
# df['key_end'] = df['key_end'].replace(np.nan, '', regex=True)

# df['key_end2'] = df['key'].str.rsplit('+_p').str[1]
# df['key_end2'] = df['key_end2'].replace('air', '_pair')
# df['key_end2'] = df['key_end2'].replace(np.nan, '', regex=True)



# # print (df['key_end'])
# df['key_new'] = df['key'].str.split('t:').str[0]
# df['key_new'] = df['key_new'].replace('count_0.alt_par', 'count_0.alt_part')

# # print (df['key_end'])
# df['keyed'] = df['key_new'] + df['key_end']
# df['keyed2'] = df['keyed'] + df['key_end2']
# print (df['keyed2'])






















# for i in p:
# 	sep = 't:'
# 	df['key'].str.split(sep, 1)[1]
# 	x.append(str(i))
# print (x)
# s = df['key'].str.split(sep, 1)[1]
# print(s)


# sep = 'count_0.alt_part'
# f = lambda x: len(df.key.split(sep, 1)[0])
# df["disappointed"] = df.apply(f, axis=1)

# # rest = df.key.split(sep, 1)[0]
# print(df["disappointed"])
# sep = 'count_1.alt_part'
# rest = df['key'].split(sep, 1)[0]
# sep = 'count_2.alt_part'
# rest = df['key'].split(sep, 1)[0]
# sep = 'count_0.ref_part'
# rest = df['key'].split(sep, 1)[0]
# sep = 'count_1.ref_part'
# rest = df['key'].split(sep, 1)[0]
# sep = 'count_2.ref_part'
# rest = df['key'].split(sep, 1)[0]
# sep = 'overlap_0.alt_part'
# rest = df['key'].split(sep, 1)[0]
# sep = 'overlap_1.alt_part'
# rest = df['key'].split(sep, 1)[0]
# sep = 'overlap_2.alt_part'
# rest = df['key'].split(sep, 1)[0]
# sep = 'overlap_0.ref_part'
# rest = df['key'].split(sep, 1)[0]
# sep = 'overlap_1.ref_part'
# rest = df['key'].split(sep, 1)[0]
# sep = 'overlap_2.ref_part'
# rest = df['key'].split(sep, 1)[0]
# sep = 'extension_0.alt_part'
# rest = df['key'].split(sep, 1)[0]
# sep = 'extension_1.alt_part'
# rest = df['key'].split(sep, 1)[0]
# sep = 'extension_2.alt_part'
# rest = df['key'].split(sep, 1)[0]
# sep = 'extension_0.ref_part'
# rest = df['key'].split(sep, 1)[0]
# sep = 'extension_1.ref_part'
# rest = df['key'].split(sep, 1)[0]
# sep = 'extension_2.ref_part'
# rest = df['key'].split(sep, 1)[0]


# files_250bp['A'] = files_250bp['A'].map(lambda x: x.rstrip('123456789').lstrip(' '))