import Bio

# Read a fasta file and align to 


from Bio.Blast import NCBIWWW


fasta_string =  open("./biopython/data/myseq.fa").read()

# Call over internet
result_handle = NCBIWWW.qblast("blastn", "nt", fasta_string)










