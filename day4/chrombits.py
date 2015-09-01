import numpy
import copy

class ChromosomeLocationBitArrays( object ):

    def __init__( self, dicts=None, fname=None ):
        # If dicts parameter provided, use to initialize
        if dicts is not None:
            arrays = dicts
        else:
            arrays = {}
        # If fname parameter provided, initialize from file
        if fname is not None: 
            for line in open( fname ):
                fields = line.split()
                name = fields[0]
                size = int( fields[1] )
                arrays[name] = numpy.zeros( size, dtype=bool )
        self.arrays = arrays

    def set_bits_from_file( self, fname ):
        for line in open( fname ):
            fields = line.split()
            # Parse fields
            chrom = fields[0]
            start = int( fields[1] )
            end = int( fields[2] )
            print self.arrays[chrom]
            self.arrays[ chrom ][ start : end ] = 1
        
    def intersect( self, other ):
        rval = {}
        for chrom in self.arrays:
            rval[chrom] = self.arrays[chrom] & other.arrays[chrom]
        return ChromosomeLocationBitArrays( dicts=rval )
        
    def union( self, other ):
        rval = {}
        for chrom in self.arrays:
            rval[chrom] = self.arrays[chrom] | other.arrays[chrom]
        return ChromosomeLocationBitArrays( dicts=rval )
        
    def complement( self ):
        rval = {}
        for chrom in self.arrays:
            rval[chrom] = ~ self.arrays[chrom]
        return ChromosomeLocationBitArrays( dicts=rval )
        
    def copy( self ):
        return ChromosomeLocationBitArrays( 
            dicts=copy.deepcopy( self.arrays ) )
        
        
    def convert(self):
        array = []
        start = None
        end = None
        print 1
        for key in self.arrays:
            status=False ###start not recording
            counter = 0
            for x, bln in enumerate(self.arrays[key]): ###begin loop
                counter += 1
                if counter%2000000==0:
                    print len(array), counter, key
                
                if status == False:  ##if not in loop
                    if bln == True: ###if the next is true
                        status = True   ####change status to true
                        start=x ### record start position
                else: ### if status is true
                    if bln ==True: ### if x is a value
                        pass
                    elif bln== False: ### falling out of the loop
                        status = False
                        end = x
                        chrom = key
                        array.append((chrom, start, end))
        return array
        
                
                
            
            #if x = True:#if integral still going on
            #else:
            #    array[chrom] = x ###if fall out array add the end spot on the list key as end
                