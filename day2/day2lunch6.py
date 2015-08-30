#!/usr/bin/env python
filename = "/Users/cmdb/qbb2015/genomes/mappedreads.sam"

f = open (filename) #opens file

dictionary ={}
count=0
total=0


for data in f:
    
    if "@" in data:
        pass
    else:    
        fields = data.split()
        total +=int(fields[4])
        count+=1
        
avg=total/count
print avg
          
#for key, value in dictionary.items():
#    print key, value       