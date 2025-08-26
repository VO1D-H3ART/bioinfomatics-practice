from DNAToolKit import *
import random



#Generate random DNA Str that is 20 Nucleotides long
randDNAStr = ''.join([random.choice(Nucleotides)
                        for nuc in range(50)])



# What this does is store the vailidated sequnce in a variable so it can be used else where
DNAStr = vaildateSeq(randDNAStr)

#print(countFreq(DNAStr))
result = countFreq(DNAStr)





