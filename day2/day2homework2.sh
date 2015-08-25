#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
annotation ="/Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"
df = pd.read_table(annotation, comment='#', header=None) ###panda opening the file ##df means dataframe  ### comment='#' ignore comments ##says no header
df.columns = ['chromosome', 'database','type','start','end','score','strand','frame','attributes']      #update column using list # updates the headers

subset = df[df['type'].str.contains('transcript')]  ###subset for type that contains transcript
subset2 = subset[subset['attributes'].str.contains('FBgn0264270')]  ###subsets for attributes that contain the gene  ### make sure when subsetting in nests use the right subset not the original

plt.figure()
plt.plot(subset2['start'])
plt.title('Sxl')
plt.xlabel("gene")
plt.ylabel('StartPosition')
plt.savefig('startsSxl2.png')
