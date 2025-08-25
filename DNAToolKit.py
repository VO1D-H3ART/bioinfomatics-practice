Nucleotides = ["A", "C", "G", "T"]


## This funciton will validate data coming in form a file
def vaildateSeq(dna_seq):
    tmpseq = dna_seq.upper()

    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
            print("There is an invalid base that is not CATG")

    return tmpseq
