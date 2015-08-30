#!/usr/bin/env python
filename = "/Users/cmdb/qbb2015/genomes/mappedreads.sam"

f = open (filename) #opens file

dictionary ={'2L':0, '2R':0, '3L':0, '3R':0, '4':0, 'X':4}


for data in f:
    
    if "@" in data:
        pass
    else:    
        fields = data.split()
        gene_name =fields[2]
        if(str(fields[2]) in dictionary):
            dictionary[str(fields[2])] +=1
print dictionary
          
#for key, value in dictionary.items():
#    print key, value              


    
    
   
        
        
