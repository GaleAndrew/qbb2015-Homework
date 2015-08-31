#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde


plot = pd.read_table("/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab")


mean=np.mean(plot2["FPKM"])
stddev=np.std(plot2["FPKM"])

x = mean + stddev * p.randn(1000)
y=p.mormpdf(plot.values, mean, stddev)

n, bins, patches = p.hist(x, 50, normed=1, histtupe='stepfilled')
p.setp(patches, 'facecolor', 'g', 'alpha', 0.75)

plt.figure()
plt.plot(bins, y, 'k--', linewidth = 1.5)
plt.savefig('density.png')


