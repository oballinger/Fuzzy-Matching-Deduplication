import os
import glob
import csv
import sys
import numpy as np
import pandas as pd
import xlrd
from pathlib import Path
import re
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from itertools import product
from fuzzywuzzy.fuzz import ratio
import string
from collections import Counter

## Input the path to the file, the filename, and the name of the column containing the values to be matched
path="/Users/ollie/folder/"
filename="filename.csv"
column="names"
output="output_filneame"

df=pd.read_csv(str(Path(path+filename)))


## Make sure all values are lowercase strings 
df[column]=df[column].str.lower()
df[column]=df[column].astype(str)

## Identify all perfect matches 
df['fullmatch'] = df[column].where(~df[column].duplicated(), 1)
matches=df.groupby(df[column].tolist(),as_index=False).size().reset_index()
matches=matches.reset_index()

## Write a loop that 
for f in range(len(df)):
	try:
		## Iteratively compare the names in each row to the whole list of names, extract the top matches to a list.
		eg=process.extractBests(df.iloc[f,5], df1[column], scorer=fuzz.token_sort_ratio)
	except:
		print(df1.iloc[f,5])
	try:
		## Write the top match to a column called "FM1_N" (fuzzy match 1, name)
		df.loc[[f],"FM1_N"]=str(eg[1]).replace("(", "").replace("'","").replace("[","").split(",")[0] 
		## Write the Levenshtein Distance score to "FM1_S" (fuzzy match 1, score)
		df.loc[[f],"FM1_S"]=str(eg[1]).replace("(", "").replace("'","").replace("[","").split(",")[1] 
	except:
		df.loc[[f],"FM1_N"]=""
		df.loc[[f],"FM1_S"]=""
	try:
		## Same process for the second best match 
		df.loc[[f],"FM2_N"]=str(eg[2]).replace("(", "").replace("'","").replace("[","").split(",")[0] 
		df.loc[[f],"FM2_S"]=str(eg[2]).replace("(", "").replace("'","").replace("[","").split(",")[1] 
	except:
		df.loc[[f],"FM2_N"]=""
		df.loc[[f],"FM2_S"]=""

	try:
		## again for the third
		df.loc[[f],"FM3_N"]=str(eg[3]).replace("(", "").replace("'","").replace("[","").split(",")[0] 
		df.loc[[f],"FM3_S"]=str(eg[3]).replace("(", "").replace("'","").replace("[","").split(",")[1] 
	except:
		df.loc[[f],"FM3_N"]=""
		df.loc[[f],"FM3_S"]=""
	print(eg)

df.to_csv(output+".csv")


