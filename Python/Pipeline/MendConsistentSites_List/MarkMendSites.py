"""
About
-----

Consolidate R dataframes that contain Mendelian consistent sites

"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pylab as p
import sklearn as sol

DEL.250bp = pd.read_csv("/Users/lmc2/Desktop/NIST/Projects/ML1-TrainingData/Code/PythonCode/Feb132017/Mendelian/MendOutput.Final/DEL/250bp.Mend.DEL.csv")
DEL.10x = pd.read_csv("/Users/lmc2/Desktop/NIST/Projects/ML1-TrainingData/Code/PythonCode/Feb132017/Mendelian/MendOutput.Final/DEL/10x.Mend.DEL.csv")
DEL.300x = pd.read_csv("/Users/lmc2/Desktop/NIST/Projects/ML1-TrainingData/Code/PythonCode/Feb132017/Mendelian/MendOutput.Final/DEL/300x.Mend.DEL.csv")
DEL.MP = pd.read_csv("/Users/lmc2/Desktop/NIST/Projects/ML1-TrainingData/Code/PythonCode/Feb132017/Mendelian/MendOutput.Final/DEL/MP.Mend.DEL.csv")
DEL.PacBio = pd.read_csv("/Users/lmc2/Desktop/NIST/Projects/ML1-TrainingData/Code/PythonCode/Feb132017/Mendelian/MendOutput.Final/DEL/PacBio.Mend.DEL.csv")
INS.250bp = pd.read_csv("/Users/lmc2/Desktop/NIST/Projects/ML1-TrainingData/Code/PythonCode/Feb132017/Mendelian/MendOutput.Final/INS/250bp.Mend.INS.csv")
INS.300x = pd.read_csv("/Users/lmc2/Desktop/NIST/Projects/ML1-TrainingData/Code/PythonCode/Feb132017/Mendelian/MendOutput.Final/DEL/300x.Mend.DEL.csv")
INS.10x = pd.read_csv("/Users/lmc2/Desktop/NIST/Projects/ML1-TrainingData/Code/PythonCode/Feb132017/Mendelian/MendOutput.Final/DEL/10x.Mend.DEL.csv")
INS.MP = pd.read_csv("/Users/lmc2/Desktop/NIST/Projects/ML1-TrainingData/Code/PythonCode/Feb132017/Mendelian/MendOutput.Final/DEL/MP.Mend.DEL.csv")
INS.PacBio = pd.read_csv("/Users/lmc2/Desktop/NIST/Projects/ML1-TrainingData/Code/PythonCode/Feb132017/Mendelian/MendOutput.Final/DEL/PacBio.Mend.DEL.csv")




new_df = pd.concat([DEL.250bp, DEL.10x, DEL.300x,DEL.MP,DEL.PacBio,INS.250bp,INS.300x,INS.10x,INS.MP,INS.PacBio], axis=0)
print new_df.head()
print new_df.shape