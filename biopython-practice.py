from Bio.Seq import Seq
from Bio import SeqIO
from Bio import Align

# This loads in a Sequnece
dna = Seq("ATCGATGCTAGCTAGGATAC")
print(dna)


# the .complement() method will return the complement of the sequence
print(dna.complement())

# this will produce the reverse complement of the dna variable
print(dna.reverse_complement())


# This for loop will loop through the entire .fasta file and return the ID, the seqence itself, and the length of the seqeunce
for sequence in SeqIO.parse("6TAP.fasta", "fasta"):
    print(sequence)
    print("length of sequence: ", len(sequence))

## CENTRAL DOGMA






