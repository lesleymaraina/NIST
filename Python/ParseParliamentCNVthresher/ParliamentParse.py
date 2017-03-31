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
start = []
end = []
ID = []
SVtype = []
SVsize = []
IlluminaGT = []
PacBioGT = []



infilename = "/Users/lmc2/Desktop/NIST/Projects/Parliament/HG002.deletions.parliament.calls.tsv"
with open(infilename, "r") as infile:
    line_list = infile.readlines()

for line in line_list:
    a = line.split('\t')
    chrom_ = a[0]
    start_ = a[1]
    end_ = a[2]
    ID_ = a[3]
    SVtype_ = a[4]
    SVsize_ = a[5]
    IlluminaGT_ = a[6]
    PacBioGT_ = a[7]
  
    chrom.append(chrom_)
    start.append(start_)
    end.append(end_)
    ID.append(ID_)
    SVtype.append(SVtype_)
    SVsize.append(SVsize_)
    IlluminaGT.append(IlluminaGT_)
    PacBioGT.append(PacBioGT_)

    # print parameters_


df = pd.DataFrame({'chrom': chrom, 
		'start': start, 
		'end': end, 
		'ID': ID, 
		'SVtype': SVtype, 
		'SVsize': SVsize, 
		'IlluminaGT': IlluminaGT, 
		'PacBioGT': PacBioGT})
	# print (df.head(8))
df['Sample'] = 'HG002'
df.to_csv('Output/DEL/HG002.deletions.parliament.calls.csv', index=False)
