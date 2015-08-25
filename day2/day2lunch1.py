#!/usr/bin/env python
filename = "/Users/cmdb/qbb2015/genomes/mappedreads.sam"

f = open (filename) #opens file

count = 0
for line in f:
    if "@"  in line:
        pass
    else:
        count +=1
    
    
    
print count