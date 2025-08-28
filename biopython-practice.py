from Bio.Seq import Seq
from Bio import SeqIO
from Bio import Align

from Bio.SeqUtils import gc_fraction

# This loads in a Sequnece
dna = Seq("ATCGATGCTAGCTAGGATAC")
print(dna)


# the .complement() method will return the complement of the sequence
print(dna.complement())

# this will produce the reverse complement of the dna variable
print(dna.reverse_complement())


# This for loop will loop through the entire .fasta file and return the ID, the seqence itself, and the length of the seqeunce
# Here we see that 

for sequence in SeqIO.parse("gene.fna", "fasta"):
    print(sequence)
    #print(sequence.seq)
    print("length of sequence: ", len(sequence))

    print ("Number of TATA boxes", sequence.count("TATA"))

    GC = gc_fraction(sequence.seq)  * 100

    # This print statment tells us: print the seqeunce ID: and the other half will return GC content rounded to 2 decimals
    print(f"{sequence.id}: {GC:.2f}%")

    ## CENTRAL DOGMA
    # Transcription:
    
    # This will return the reverse complement of the given sequence
    template_dna = sequence.reverse_complement()
    #print(template_dna)

    full_seq = sequence.seq

    mRNA = full_seq.transcribe()
    #print("mRNA: \n", mRNA)

    # back-transcription
    coding_dna = mRNA.back_transcribe()
    #print("Back-Transcibe: \n", coding_dna)

    # Translation: converts to protein
    #print("Tranlation: ", mRNA.translate())









