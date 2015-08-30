#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pylab as p

plot = pd.read_table("/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab")
roi = plot['FPKM'] >0
plot2=plot[roi]['FPKM']
plot3=np.log(plot2)

mean=np.mean(plot3)
stddev=np.std(plot3)


x = mean + stddev * p.randn(1000)

#n, bins, patches = p.hist(x, 50, normed=1, histtype='stepfilled')
#p.setp(patches, 'facecolor', 'g', 'alpha', 0.75)


#y = p.normpdf(bins, mean, stddev)

x.sort() ###gets in order



plt.figure()
plt.hist(list(plot3))
y = p.normpdf(x, mean, stddev)
#plt.hist(plot.values)
plt.plot(x,y*len(plot2),'r--')


plt.title('Density Plot')
plt.xlabel('log of fpkm')
plt.ylabel('frequency')
#plt.show()
plt.savefig('density.png')


