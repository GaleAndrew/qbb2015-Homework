#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plot = pd.read_table("/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab")
roi = plot['FPKM'] >0

plot2=plot[roi]['FPKM']
plot3=np.log(plot2)

plt.figure()
plt.hist(plot3.values)
plt.xlabel('log of fpkm')
plt.ylabel('frequency')
plt.savefig("histo.png")