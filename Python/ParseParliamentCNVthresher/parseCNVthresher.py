################################################
#About 
#Date: Aug 22, 2016
#Store VCF File contents in a CSV file
##source: http://stackoverflow.com/questions/28043834/attributeerror-list-object-has-no-attribute-close-for-reading-one-file
################################################
import requests, re, sqlite3
from pyquery import PyQuery
from collections import Counter
import os
import glob
import pandas as pd 

chrom = []
name = []
SVtype = []
start = []
end = []
holder1 = []
holder2 = []
holder3 = []
parameters = []


infilename = "/Users/lmc2/Desktop/NIST/Projects/CNVthresher/HG002.adjusted_union_sites_deletions2.out.tsv"
with open(infilename, "r") as infile:
    line_list = infile.readlines()

for line in line_list:
    a = line.split('\t')
    chrom_ = a[0]
    name_ = a[1]
    SVtype_ = a[2]
    start_ = a[3]
    end_ = a[4]
    holder1_ = a[5]
    holder2_ = a[6]
    holder3_ = a[7]
    parameters_ = a[8]
  
    chrom.append(chrom_)
    name.append(name_)
    SVtype.append(SVtype_)
    start.append(start_)
    end.append(end_)
    holder1.append(holder1_)
    holder2.append(holder2_)
    holder3.append(holder3_)
    parameters.append(parameters_)

    # print parameters_


df = pd.DataFrame({'chrom': chrom, 
		'name': name, 
		'SVtype': SVtype, 
		'start': start, 
		'end': end, 
		'holder1': holder1, 
		'holder2': holder2, 
		'holder3': holder3,
        'parameters': parameters})
	# print (df.head(8))
# df.to_csv('hg2CNVthresh.csv', index=False)

# print df.head()

def title(name):
    temp_1 = name.split(';')[0] 
    return temp_1

def title2(name):
    temp_1 = name.split('=')[1]
    return temp_1

def title3(name):
    temp_1 = name.split(';')[1]
    return temp_1

def title4(name):
    temp_1 = name.split(';')[2] 
    return temp_1

def title5(name):
    temp_1 = name.split(';')[3]
    return temp_1

def title6(name):
    temp_1 = name.split(';')[4]
    return temp_1

def title7(name):
    temp_1 = name.split(';')[5]
    return temp_1

def title8(name):
    temp_1 = name.split(';')[6]
    return temp_1

def title9(name):
    temp_1 = name.split(';')[7]
    return temp_1

def title10(name):
    temp_1 = name.split(';')[8]
    return temp_1

def title11(name):
    temp_1 = name.split(';')[9]
    return temp_1

def title12(name):
    temp_1 = name.split(';')[10]
    return temp_1

def title13(name):
    temp_1 = name.split(';')[11]
    return temp_1

def title14(name):
    temp_1 = name.split(';')[12]
    return temp_1

def title15(name):
    temp_1 = name.split(';')[13]
    return temp_1

df1 = df['parameters'].apply(title)
df['scbp1/2'] = df1.apply(title2)

df2 = df['parameters'].apply(title3)
df['scf1/2'] = df2.apply(title2)

df3 = df['parameters'].apply(title4)
df['fbiall'] = df3.apply(title2)

df4 = df['parameters'].apply(title5)
df['funbal'] = df4.apply(title2)

df5 = df['parameters'].apply(title6)
df['mscore'] = df5.apply(title2)

df6 = df['parameters'].apply(title7)
df['ncov'] = df6.apply(title2)

df7 = df['parameters'].apply(title8)
df['dcov'] = df7.apply(title2)

df8 = df['parameters'].apply(title9)
df['sdcov'] = df8.apply(title2)

df9 = df['parameters'].apply(title10)
df['sharp'] = df9.apply(title2)

df10 = df['parameters'].apply(title11)
df['fgood'] = df10.apply(title2)

df11 = df['parameters'].apply(title12)
df['ninsize'] = df11.apply(title2)

df12 = df['parameters'].apply(title13)
df['fQ0'] = df12.apply(title2)

df13 = df['parameters'].apply(title14)
df['fQ0flank'] = df13.apply(title2)

df14 = df['parameters'].apply(title15)
df['fNonRef'] = df14.apply(title2)


# NOTE: Difficult to parse becasue some rows are missing: scbp1/2, scf1/2


print df.head()
# train.to_csv('df34.csv')