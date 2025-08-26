import collections


Nucleotides = ["A", "C", "G", "T"]


## This funciton will validate data coming in form a file
# This also really hates spaces

# The reason we are using TmpSeq here is because it has been converted to uppercase from the original dna_seq value
# this is to make a safe working copy as to not override the orignal input


def vaildateSeq(dna_seq):
    tmpseq = dna_seq.upper()

    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
            print("There is an invalid base that is not CATG")

    return tmpseq




# The for loop will loop throw nuc (CATG) and tmpFreqDict[nuc] will add 1 to the dict where ever apporitate
# remeber that seq is the user input
# The dictionary must start everything at 0 and start counting
def countFreq(seq):
    tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nuc in seq:
        tmpFreqDict[nuc] += 1
        
    return tmpFreqDict
    #return dict(collections.Counter(seq)) <-- This is an optimaization that can replace the 4 lines above it
