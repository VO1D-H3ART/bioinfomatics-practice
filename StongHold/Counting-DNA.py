DNAseq = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

def countFreq(seq):
    tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nuc in seq:
        tmpFreqDict[nuc] += 1
        
    return tmpFreqDict

#print(countFreq(DNAseq))
result = countFreq(DNAseq)


print(' '.join([str(val) for key, val in result.items()]))