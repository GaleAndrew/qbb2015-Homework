#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"

f = open (filename) #opens file

for line in f:
    fields = line.split()       ### creates fields for the lines and splits them into lists based on the whitespace
    if"tRNA" in fields[9]:     ### specifies that tRNA has to be in the ninth list or theth column
        print line,   #### comma stops new line in print  ##line is not a special word just a variable
    

