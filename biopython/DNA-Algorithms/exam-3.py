
fasta_path = "./biopython/data/chr1.GRCh38.excerpt.fasta"

genome = readGenome(fasta_path)

#Q1 3
p = 'GCTGATCGATCGTACG'

bm, bs = naive_leniant_best_match(p, genome, editDistance, keep= 1)
# Verify
editDistance(p, genome[bm[0]:bm[0]+len(p)])

#Q2 2
p = 'GATTTACCAGATTGAG'

bm, bs = naive_leniant_best_match(p, genome, editDistance, keep= 1)
# Verify
editDistance(p, genome[bm[0]:bm[0]+len(p)])

# Q3 Edges? 904746

reads, quals = readFastq('./biopython/data/ERR266411_1.for_asm.fastq')

overlap_k = 30
k = overlap_k
len(reads)

def create_kmer_relations(reads, k):
    rels = dict()
    for read_i, read in enumerate(reads):
        for i in range(len(read)-k+1):
            kmer = read[i:i+k]
            if kmer in rels:
                rels[kmer].add(read_i)
            else:
                rels[kmer] = set([read_i])
    return rels

rels = create_kmer_relations(reads, overlap_k)

pairs = list()
for base_i, base_read in enumerate(reads):
    suffix = base_read[-k:]
    for compare_read_i in rels[suffix]:
        if base_i == compare_read_i:
            continue
        compare_read = reads[compare_read_i]
        ovelap_score = overlap(base_read, compare_read, min_length=k)
        if ovelap_score > 0:
            pairs.append((base_i, compare_read_i))

len(pairs)

ai = 6062
bi = 5114
overlap(reads[ai], reads[bi])

# Q4 Nodes with one 7161
output_nodes = set()
for (src, dst) in pairs:
    output_nodes.add(src)

len(output_nodes)

pairs = list()
for base_i, base_read in enumerate(reads):
    for compare_read_i, compare_read in enumerate(reads):
        if base_i == compare_read_i:
            continue
        ovelap_score = overlap(base_read, compare_read, min_length=k)
        if ovelap_score > 0:
            pairs.append((base_i, compare_read_i))

a = 'GCTTTGGCCTCTATTAAGCTCATTCAGGCTTCTGCCGTTTTGGATTTAACCGAAGATGATTTCGATTTTCTGACTAGTAACAAAGTTTGGATTGCTACTG'
b = 'AAGGTAAACGCGAACAATTCAGCGGCTTTAACCGGACGGTCGGCCCCGATAATAATGATTGCCGTAAATTCAGGGCTTTCCAGGATTAGGCAGGCCGTTT'

overlap(a,b)


