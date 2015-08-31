#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



plota = pd.read_table("/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab")
plotb= pd.read_table("/Users/cmdb/qbb2015/stringtie/SRR072894/t_data.ctab")
R = plota['FPKM']
G = plotb['FPKM']

M = np.log2([R/G])
A = .5*np.log2([R*G])

#print type(A)

#print type(M)
#A=np.array(A)
#M=np.array(M)
#heatmap, xedges, yedges = np.histogram2d(M, A, bins=50)
#extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

#plt.clf()
#plt.imshow(heatmap, extent=extent)
#plt.show()



plt.figure()
plt.scatter(A,M)
plt.xlabel('Data distribution')
plt.ylabel('Log 2fold Difference')
plt.title("Comparison MA Plot")
#plt.show()
plt.savefig("MA.png")