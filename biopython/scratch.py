import Bio

# Read a fasta file and align to 


from Bio.Blast import NCBIWWW, NCBIXML


fasta_string =  open("./biopython/data/myseq.fa").read()

# Call over internet
result_handle = NCBIWWW.qblast("blastn", "nt", fasta_string)
result_handle
blast_record = NCBIXML.read(result_handle)

help(blast_record)
dir(blast_record)

dir(blast_record.descriptions[0])
blast_record.descriptions[0].title

mine = 10000000
current_d = None
for d in blast_record.descriptions:
    if d.e < mine:
        mine = d.e
        current_d = d


current_d.title

from Bio.Seq import Seq

Seq.translate(dnaseq)
dna = 'atgc'
print(reverse complemetn is %s' % dna)


dna = 'TGGGCCTCATATTTATCCTATATACCATGTTCGTATGGTGGCGCGATGTTCTACGTGAATCCACGTTCGAAGGACATCATACCAAAGTCGTACAATTAGGACCTCGATATGGTTTTATTCTGTTTATCGTATCGGAGGTTATGTTCTTTTTTGCTCTTTTTCGGGCTTCTTCTCATTCTTCTTTGGCACCTACGGTAGAG'

dnaseq = Seq(dna)

type(dnaseq)
dnaseq


