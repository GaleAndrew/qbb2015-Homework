class BLASTReader(object):
    def __init__(self, file):
        self.file =open(file)
        self.last_ident=None
        
    def next(self):
        if self.last_ident==None:
            line=self.file.readline()
           # assert line.startswith('>'), "Not Valid Fasta"
            ident=line[1:].strip('\r\n')  ##strip on white
        else:
            ident=self.last_ident

        sequences=[]
        while True:
             
            line=self.file.readline()
            if not line:
                break
            if line.startswith('>'):
                self.last_ident=line[1:].lstrip('> ')
                sequences.append(line.strip())
  
            if line.startswith(' Identities'):
                sequences.append(line.strip())
                break
         
                
                
        if len(sequences)==0:
            raise StopIteration

        sequence=''.join(sequences)  ###whater in' join sequences with it in between
        return ident, sequence
        
    def __iter__(self):
        return self