from DNAToolKit import *
import random


#Generate random DNA Str that is 20 Nucleotides long
randDNAStr = ''.join([random.choice(Nucleotides)
                        for nuc in range(50)])




print(vaildateSeq(randDNAStr))
print(countFreq(randDNAStr))

