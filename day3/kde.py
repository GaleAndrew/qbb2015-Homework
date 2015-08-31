#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde


plot = pd.read_table("/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab")
roi = plot['FPKM'] >0

plot2=plot[roi]['FPKM']
plot3=np.log(plot2)
#plot2['ordinal'] = [x.toordinal() for x in df.dates]
mu=np.mean(plot2)
xi=np.std(plot2)
#density = gaussian_kde(plot2)
#density.covariance_factor = lambda : .25
#density._compute_covariance()



