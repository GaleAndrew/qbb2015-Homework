#!/usr/bin/env python
filename = "/Users/cmdb/qbb2015/genomes/mappedreads.sam"

f = open (filename) #opens file


count = 0
for line in f:
    if "NH:i:1" in line:
        count +=1
    else:
        pass
    
    
    
print count