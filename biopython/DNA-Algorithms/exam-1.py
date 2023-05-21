from collections import Counter

def readGenome(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            # ignore header line with genome information
            if not line[0] == '>':
                genome += line.rstrip()
    return genome

def naive(p, t):
    occurrences = []
    for i in range(len(t) - len(p) + 1):  # loop over alignments
        match = True
        for j in range(len(p)):  # loop over characters
            if t[i+j] != p[j]:  # compare characters
                match = False
                break
        if match:
            occurrences.append(i)  # all chars matched; record
    return occurrences


def reverseComplement(s):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'N': 'N'}
    t = ''
    for base in s:
        t = complement[base] + t
    return t

def readFastq(filename):
    sequences = []
    qualities = []
    with open(filename) as fh:
        while True:
            fh.readline()  # skip name line
            seq = fh.readline().rstrip()  # read base sequence
            fh.readline()  # skip placeholder line
            qual = fh.readline().rstrip() # base quality line
            if len(seq) == 0:
                break
            sequences.append(seq)
            qualities.append(qual)
    return sequences, qualities


def lenient_naive(p, t, max_error = 2):
    occurrences = []
    for i in range(len(t) - len(p) + 1):  # loop over alignments
        match = True
        num_err = 0
        for j in range(len(p)):  # loop over characters
            if t[i+j] != p[j]:  # compare characters
                num_err += 1
                if num_err > max_error:
                    match = False
                    break
        if match:
            occurrences.append(i)  # all chars matched; record
    return occurrences


genome_file_path = "./biopython/data/lambda_virus.fa"
genome = readGenome(genome_file_path)

##################
# 1. How many times does AGG or its reverse complement (ACCT) occur in the lambda virus genome?
################
p = 'AGGT'

len(naive(p, genome)) + len(naive(reverseComplement(p), genome))

genome.count(p) + genome.count(reverseComplement(p))

genome.count('TTAA')

# Q3
p = 'ACTAAGT'
min(naive(p, genome)[0], naive(reverseComplement(p), genome)[0]) 

# Q4
p = 'AGTCGA'
min(naive(p, genome)[0], naive(reverseComplement(p), genome)[0]) 

# Q5
p = 'TTCAAGCC'

len(lenient_naive(p, genome, max_error=2))

p = 'AGGAGGTT'
lenient_naive(p, genome, max_error=2)[0]

#Q7
fastq_path = './biopython/data/ERR037900_1.first1000.fastq'
seqs, quals =readFastq(fastq_path)

import numpy as np
seq_lens = [len(s) for s in seqs]
scores = np.array([[ord(c)-33 for c in q] for q in quals])
mean_score = scores.mean(axis=0)

mean_score.argmin()




