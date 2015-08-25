#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"

f = open (filename) #opens file

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
for line_count,line in enumerate(f):
    if line_count <=10:
        pass 
    elif line_count <=15:
        print line,
    else:
        break