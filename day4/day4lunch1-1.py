#!/usr/bin/env python

""""
Count intersection of the two BED files
"""
from __future__ import division

import sys 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib_venn import venn3, venn3_circles

def arrays_from_len_file (fname):
    arrays ={}
    for line in open(fname): ###split into fields, take name of chromosome under name, take the size by turning the str into an int. the int is turned into the size variable. the arrays is given the name of the chromosome then using the np.zeros( size) it makes the array filled with zeroes based on the the int size (think unciruclarizing DNA and making each bp a 0)
        fields = line.split() #split columns
        name =fields[0]         #name is in column 0
        size =int(fields[1])    #size is in comumn 1
        arrays[name]=np.zeros(size, dtype = bool)  #### into arrays add the namecreate an array that is filled with zeroes### stores based on size true of false #name is the key of the dict and the right of it is saying its zeroes of size then datatype thats a bool
    return arrays
    
def set_bits_from_file(arrays,fname):
    for line in open(fname):
        fields =line.split()
        #parse fields
        chrom = fields[0]
        start = int(fields[1])
        end = int(fields[2])
        arrays[chrom][start:end] = 1 #edits the array with chrom as key and start end as values gives a 1 to every position in the slice
###all 3    



arrays1 = arrays_from_len_file(sys.argv[1])
arrays2 = arrays_from_len_file(sys.argv[1])
arrays3 = arrays_from_len_file(sys.argv[1])
arrays4 = arrays_from_len_file(sys.argv[1])
arrays5 = arrays_from_len_file(sys.argv[1])
arrays6 = arrays_from_len_file(sys.argv[1])
modify2 =set_bits_from_file(arrays1, sys.argv[2])
modify22 =set_bits_from_file(arrays2, sys.argv[2])
modify3 =set_bits_from_file(arrays3, sys.argv[3])
modify33 =set_bits_from_file(arrays4, sys.argv[3])
modify4 =set_bits_from_file(arrays5, sys.argv[4])
modify44 =set_bits_from_file(arrays6, sys.argv[4])

count1 =0
count2 =0
count3 =0
count4 =0
count5 =0
count6 =0
count7 =0
total=0

#1
#2
#3
#4
#if A B C
#then +1 ABC
#if A
#elif B
#elif C
#elif A B


for filename in sys.argv[2:]:
    for line in open(filename):
        fields =line.split()
      #  #parse fields
        chrom = fields[0]
        start = int(fields[1])
        end = int(fields[2])
        #get slice
        sl1 = arrays1[chrom][start:end]
        sl2 = arrays3[chrom][start:end]
        sl3 = arrays5[chrom][start:end]
        
        if sl1.all() & sl2.all() & sl3.all(): #all
            count7 += 1
        elif sl1.all() & sl2.all() &~ sl3.all(): #23
            count6 += 1
        elif sl1.all() &~ sl2.all() & sl3.all():#34
            count5 += 1
        elif sl3.all() & sl2.all() &~sl1.all(): #24
            count4 += 1
        elif sl1.all() &~ sl2.all() &~ sl3.all(): #2
            count3 += 1
        elif sl3.all() &~ sl2.all() &~ sl1.all(): #3
            count2 += 1
        else:
            count1+=1  #4
print count7 
print count6
print count5 
print count4 
print count3 
print count2 
print count1  
        
        #total+=1
       # any_overlap += sl.any() #looks at all position in slice if all false any returns alse/0 if any true any returns true/1
        #all_overlap+=sl.all() #if all true return 1 if any false return 0
        #50%overlap 
        #half_overlap+=(np.sum(sl)/len(sl)>0.5)
    #print "Total %d, Any overlap %d all overlap %d half_overlap %d" % (total, any_overlap, all_overlap,half_overlap)
    

plt.figure()
venn3(subsets=(count1, count2,count6,count3,count4,count6,count7), set_labels = ('SuHW','CTCF','BEAF'))
plt.savefig("Venn.png")
#plt.show()




