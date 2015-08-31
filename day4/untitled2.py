#!/usr/bin/env python

""""
Count intersection of the two BED files
"""
from __future__ import division
import matplotlib.pyplot as plt
from matplotlib_venn import venn3, venn3_circles
import sys 

import chrombits
    
    
print 1    
print "hello"  
    
arr=chrombits.ChromosomeLocationBitArrays(fname=sys.argv[1])
#arr=chrombits.ChromosomeLocationBitArrays( fname=sys.argv[1] )

print 2
ctcf=arr.copy()
beaf = arr.copy()
suhw = arr.copy()

print 3
ctcf.set_bits_from_file(sys.argv[2])
beaf.set_bits_from_file(sys.argv[3])
suhw.set_bits_from_file(sys.argv[4])

print 4
### will return those in beaf and ctcf
#new=beaf.intersect(ctcf.complement())
#ranges=new.convert()
#for x in ranges:
#    print x
print 5
new = beaf.union(ctcf.union(suhw))


convertnew=new.convert()
#print ranges

#arrays1 = chrombits.ChromosomeLocationBitArrays(new)
#arrays2 = chrombits.ChromosomeLocationBitArrays(new)
#arrays3 = chrombits.ChromosomeLocationBitArrays(new)
#arrays4 = chrombits.ChromosomeLocationBitArrays(fname =sys.argv[1])
#arrays5 = chrombits.ChromosomeLocationBitArrays(fname =sys.argv[1])
#arrays6 = chrombits.ChromosomeLocationBitArrays(fname =sys.argv[1])
#arrays1.set_bits_from_file( sys.argv[2])
#arrays2.set_bits_from_file( sys.argv[3])
#arrays3.set_bits_from_file( sys.argv[4])
print 6

count1 =0
count2 =0
count3 =0
count4 =0
count5 =0
count6 =0
count7 =0
#total=0
print 7
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

for chrom, start, end in convertnew:
    sl1 = ctcf.arrays[chrom][start:end]
    sl2 = beaf.arrays[chrom][start:end]
    sl3 = suhw.arrays[chrom][start:end]
#        
    if sl1.any() and sl2.any() and sl3.any(): #all
        count7 += 1
    elif sl1.any() and sl2.any() and not sl3.any(): #23
        count6 += 1
    elif sl1.any() and not sl2.any() and sl3.any():#34
        count5 += 1
    elif sl3.any() and sl2.any() and not sl1.any(): #24
        count4 += 1
    elif sl1.any() and not sl2.any() and not sl3.any(): #2
        count3 += 1
    elif sl3.any() and not sl2.any() and not sl1.any(): #3
        count2 += 1
    else:
        count1+=1  #4
#for filename in sys.argv[2:]:
#    for line in open(filename):
#        fields =line.split()
      #  #parse fields
#        chrom = fields[0]
#        start = int(fields[1])
#        end = int(fields[2])
        #get slice
        
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
plt.savefig("Vennday52.png")
plt.show()


