#!/usr/bin/env python
 

import sys
import numpy as np
from blastscore import BLASTScore
import matplotlib.pyplot as plt
 

reader=BLASTScore(sys.argv[1])

list1=[]
list2=[]
for i, (score, evalue) in enumerate(reader):
#    print type(score)
#    print type(evalue)
   
    list1.append(float(score))
    list2.append(float(evalue))
list1a=np.log(list1)
list2a=np.log(list2)
#print list1
#list1a=np.log(list1)
#list2a=np.log(list1)
#list1a=int(list1)


plt.figure()
plt.title('Scores')
plt.xlabel('Score')
plt.ylabel('Frequency of Score')
plt.hist(list1, bins=(50,100,150,200,250,300,350,400))
#plt.show() 
plt.savefig('Scores.png')



plt.figure()
plt.title('Evalues')
plt.xlabel('Evalues')
plt.ylabel('Frequency of Evalues')
plt.hist(list2, bins=(10))
#plt.show() 
plt.savefig('evalues.png')


plt.figure()
plt.scatter(list1a,list2a)
#plt.show()
plt.title('Evalues Vs Scores')
plt.xlabel('Score')
plt.ylabel('Evalues')
plt.savefig('Scoresvsevalues.png')






