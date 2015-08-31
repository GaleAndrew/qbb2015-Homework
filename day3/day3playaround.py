#!/usr/bin/env python
#####make a KDE without the histogram 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np




plot = pd.read_table("/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab")
roi = plot['FPKM'] >0

plot2=plot[roi]['FPKM']
plot3=np.log(plot2)

plt.figure()
plot3.plot(kind = 'kde')
plt.show()