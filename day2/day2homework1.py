#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
annotation ="/Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"
df = pd.read_table(annotation, comment='#', header=None) ###panda opening the file ##df means dataframe  ### comment='#' ignore comments ##says no header
df.columns = ['chromosome', 'database','type','start','end','score','strand','frame','attributes']      #update column using list # updates the headers


roi=df['frame'].str.contains('FBgn0264270')
plt.figure()
#plt.plot(df[roi]['start'])
plt.title(Sxl)
plt.xlabel("gene")
plt.ylabel('StartPosition')
plt.savefig('starts2R.png')
