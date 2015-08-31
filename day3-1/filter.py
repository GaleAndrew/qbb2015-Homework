#!/usr/bin/env python



#filename = "/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab" ##oull specific file
import sys   ###imports sys

###open using aguements
#print sys.argv    ###says take whatever is on there beyone the script so script then file ...
#filename = sys.argv[1]  ### filename is going to be the first arguement after the 0 position (code in the example) sys.argv[1:] would mean 1 to end will be files etc 


#f = open (filename) #opens file
#### ends opening with arguements


f = sys.stdin ##example cat /Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab | ./filter.py | head##
                ###example 2 ./filter.py < /Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab 


#for line in f:
#    fields = line.split()       ### creates fields for the lines and splits them into lists based on the whitespace
#    if"tRNA" in fields[9]:     ### specifies that tRNA has to be in the ninth list or theth column
#        print line,   #### comma stops new line in print  ##line is not a special word just a variable
        
###########################################################################    
#line_count = 0
#iterate teh file line by line
#for line in f:
#    if line_count <=10:
    #    pass 
 #   elif line_count <=15:
   #     print line,
  #  else:
#        break
 #   line_count+=1    ## will read lines only print 11 to 15 and break after 15
    
    
##############################################################################
### prints only set of lines but will not read the rest of the lines
#for line_count,line in enumerate(f):
#    if line_count <=10:
#        pass 
#    elif line_count <=15:
#        print line,
#    else:
#        break

## find and counts the number of times a gene name appears stores in dict
name_counts = {}
for line_count, data in enumerate(f):
    fields = data.split()
    gene_name =fields[9]
    if gene_name not in name_counts:
        name_counts[gene_name]=1
    else:
        name_counts[gene_name]+=1 

## iterate keym value pairs from the name counts dictionary
for  key, value in name_counts.iteritems():
    ##print anme and count
    print key, value

        
        
        
        
        
        
        
        
        
        
        