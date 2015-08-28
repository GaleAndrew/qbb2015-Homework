#!/usr/bin/env python

""""
Count intersection of the two BED files
"""
from __future__ import division

import sys 

import chrombits
    
    
    
    
    
arr=chrombits.ChromosomeLocationBitArrays(fname=sys.argv[1])
#arr=chrombits.ChromosomeLocationBitArrays( fname=sys.argv[1] )


ctcf=arr.copy()
beaf = arr.copy()
suhw = arr.copy()


ctcf.set_bits_from_file(sys.argv[2])
beaf.set_bits_from_file(sys.argv[3])
suhw.set_bits_from_file(sys.argv[4])


### will return those in beaf and ctcf
new=beaf.intersect(ctcf.complement())
ranges=new.convert()
for x in ranges:
    print x

new = beaf.union(ctcf.union(suhw))


ranges=new.convert()


print ranges