#!/usr/bin/env python

import pandas as pd
#import matplotlib.pyplot as plt
annotation ="/Users/cmdb/qbb2015/rawdata/samples.csv"
df = pd.read_csv(annotation) ###panda opening the file ##df means dataframe  ### comment='#' ignore comments ##says no header
#df.columns = ['chromosome', 'database','type','start','end','score','strand','frame','attributes']      #update column using list # updates the headers


for x in df['sample']:
 
   
    variable = pd.read_table("/Users/cmdb/qbb2015/stringtie/"+x+"/t_data.ctab")
    roi=variable['t_name'].str.contains('FBtr0331261')
    print variable[roi]
    