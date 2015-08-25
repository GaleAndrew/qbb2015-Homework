#!/usr/bin/env python

import pandas as pd

annotation ="/Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"

df = pd.read_table(annotation, comment='#', header=None) ###panda opening the file ##df means dataframe  ### comment='#' ignore comments ##says no header

#print df

#print df.head() #first 5 lines

#print df.describe() #gives some statistics


#print df.info()

#specific rows

#print df[1:5] #prints 1-4  end number non-inclusive can start at zeroeth row

#/n = new line

#show rows 10 to 15

#print df[9:15]

#show 20 to 25
#print df[19:25]

#print columns
df.columns = ['chromosome', 'database','type','start','end','score','strand','frame','attributes']      #update column using list # updates the headers

#print df.sort("type")

#subset (column) chrmoosome start and end
#print df[['chromosome', 'start', 'end']]  #must pass it multiple as a list


#filter both row and column this is column then row order does not matter can do row then column
#print df['start'][9:15]

#print df.shape
#df2 = df['start']
#print df2.shape



#save to a new file

#df2.to_csv('startColumn.txt', sep='\t',index=False) #will not have the first comma


#search for something 
#boolean filtering
#find features whos start value is less than 10 (strings are harder)

#roi = df['start'] < 10
#print df[roi]    #~is binary not so it will act as a not










