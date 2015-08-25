#!/usr/bin/env python
filename = "/Users/cmdb/qbb2015/genomes/mappedreads.sam"

f = open (filename) #opens file

dictionary ={}


for data in f:
    
    if "@" in data:
        pass
    else:    
        fields = data.split()
        gene_name =fields[2]
        if "2L" or "2R" or "3L" or "3R" or "4" or "X" in gene_name:
            if gene_name not in dictionary:
                dictionary[gene_name]=1
            else:
                 dictionary[gene_name]+=1 
          
for key, value in dictionary.items():
    print key, value              

            
       
            
    
    
   
        
        
