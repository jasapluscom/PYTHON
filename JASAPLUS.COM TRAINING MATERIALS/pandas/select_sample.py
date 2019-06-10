#!/usr/bin/env python3
'''
sample loc, iloc and ix
for python training at www.jasaplus.com
'''
import pandas as pd
df = pd.read_csv("sample.csv")
print("=============loc sample")
loc1 =  (df.loc[:,'phone'])
print(loc1)
print(df.loc[:,'phone'])
print(df.loc[:,'name'])
print(df.loc[0, :])
print(df.loc[0])
print(df.loc[:])
print(df.loc[:])
print(df.loc[:,'name'])
print("=============iloc sample")

#rows
print(df.iloc[0]) # first row of data frame
print(df.iloc[1]) # second row of data frame
print(df.iloc[-1]) # last row of data frame
#columns
print(df.iloc[:,0]) # first column of data frame
print(df.iloc[:,1]) # second column of data frame
print(df.iloc[:,-1]) # last column of data frame

print("=============ix sample")

print(df.ix[0])
print(df.ix[0, 'name'])
print(df.ix[0, 0])
