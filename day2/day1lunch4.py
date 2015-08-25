#!/usr/bin/env python
filename = "/Users/cmdb/qbb2015/genomes/mappedreads.sam"

f = open (filename) #opens file
line_count = 0
for line_count,data in enumerate(f):
    if line_count <=9:
        fields = data.split()
        chromosome =fields[1]
        print chromosome
    else:
        pass