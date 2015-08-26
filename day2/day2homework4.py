#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

plot = pd.read_table("/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab")
roi = plot['FPKM'] >0
#plot2=plot/sort("FPKM")

plot2=plot[roi]['FPKM'] 
#print plot2
#count = plot2.count()
#print count
#third = count/3
#print third
#firstthird = "0-3182"
#secondthird = "3182-6365"
#lastthird = "6365-9549"

top = plot2[0:3182]
middle = plot2[3182:6365]
bottom = plot2[6365:9549]




# = plot2[roi1]
#pplot2 = plot2[roi2]
#pplot3 = plot2[roi3]


plt.figure()
plt.title('Excercise 4')
plt.boxplot([top, middle, bottom])
plt.xlabel("gene")
plt.ylabel('StartPosition')
plt.savefig('day2homework4.png')

