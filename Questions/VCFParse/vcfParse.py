#!/usr/bin/env python
##########################################################################
# ABOUT
# Date: Nov 25, 2016
# Notes:
# Code to save each line of a VCF file in an individual VCF file
##########################################################################

##########################################################################
# IMPORTS
##########################################################################

import pandas as pd 

##########################################################################
# DATA IMPORT
##########################################################################

# changed the vcf file path from .vcf to .txt manually
test = open('vcf2.txt', 'r')
test_lines = test.readlines()
test.close()
print(test_lines[0])


# Store a List in a CSV
lines = []
sp = test_lines[0]
lines.append(sp)
sq = pd.DataFrame(lines)
sq.to_csv ('newFile.csv')




