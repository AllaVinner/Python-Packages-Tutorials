

fasta_path = "./biopython/data/chr1.GRCh38.excerpt.fasta"

genome = readGenome(fasta_path)


# Q1 799954
p = 'GGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGG'
len(genome) - len(p)+1

#Q2 984143
def naive_with_stats(p, t):
    occurrences = []
    alignments = 0
    char_checks = 0
    for i in range(len(t) - len(p) + 1):  # loop over alignments
        match = True
        alignments += 1
        for j in range(len(p)):  # loop over characters
            char_checks += 1
            if t[i+j] != p[j]:  # compare characters
                match = False
                break
        if match:
            occurrences.append(i)  # all chars matched; record
    return occurrences, alignments, char_checks

hits, al, ch = naive_with_stats(p, genome)
al
ch

#Q3 165191 :( 127974

def boyer_more_with_stats(p, p_bm, t):
    i = 0
    occurerences = list()
    alignments =0 
    char_comparisons = 0
    while i < len(t) - len(p) + 1:
        shift = 1
        alignments += 1
        mismatched = False
        for j in range(len(p) -1, -1, -1):
            char_comparisons += 1
            if p[j] != t[i+j]:
                skip_bc = p_bm.bad_character_rule(j, t[i+j])
                skip_gs = p_bm.good_suffix_rule(j)
                shift = max(shift, skip_bc, skip_gs)
                mismatched = True
                break
        if not mismatched:
            occurerences.append(i)
            skip_gs = p_bm.match_skip()
            shift = max(shift, skip_gs)
        i += shift
    return occurerences, char_comparisons, alignments

p_bm = BoyerMoore(p)
occ, ch, al = boyer_more_with_stats(p, p_bm, genome)
ch
occ
al

# Q 4 40, 19
import bisect
genome_index = Index(genome, 8)

genome_index.query("AAAAAAAA")
p = 'GGCGCGGTGGCTCACGCCTGTAAT'


def hamming_distance(p1, p2):
    dist = 0
    for i in range(len(p1)):
        if p1[i] != p2[i]:
            dist += 1
    return dist

def find1(p, genome_index, genome, max_error = 2):
    k = 8
    n = 24

    p1 = p[:k]
    p2 = p[k:2*k]
    p3 = p[2*k:]

    p1_matches = genome_index.query(p1)
    print(f"p1 hits: {len(p1_matches)}")
    p2_matches = genome_index.query(p2)
    print(f"p3 hits: {len(p2_matches)}")
    p3_matches = genome_index.query(p3)
    print(f"p3 hits: {len(p3_matches)}")

    matches = set()

    for p1_match in p1_matches:
        if p1_match + n >= len(genome):
            continue
        if hamming_distance(genome[p1_match: p1_match + n], p) <= max_error:
            matches.add(p1_match)
    
    for p2_match in p2_matches:
        if p2_match - k + n >= len(genome) or p2_match - k < 0:
            continue
        if hamming_distance(genome[p2_match-k: p2_match-k + n], p) <= max_error:
            matches.add(p2_match-k)
    
    for p3_match in p3_matches:
        if p3_match - 2*k < 0 or p3_match + k >= len(genome):
            continue
        if hamming_distance(genome[p3_match-2*k: p3_match + k], p) <= max_error:
            matches.add(p3_match-2*k)
    
    return matches

o = find1(p, genome_index, genome)
len(o)

# Q5 - 90 was correct
p = 'GGCGCGGTGGCTCACGCCTGTAAT'
len(p)
o = find1(p, genome_index, genome)
len(o)

#Q6 59, 79

class SubseqIndex(object):
    """ Holds a subsequence index for a text T """
    
    def __init__(self, t, k, ival):
        """ Create index from all subsequences consisting of k characters
            spaced ival positions apart.  E.g., SubseqIndex("ATAT", 2, 2)
            extracts ("AA", 0) and ("TT", 1). """
        self.k = k  # num characters per subsequence extracted
        self.ival = ival  # space between them; 1=adjacent, 2=every other, etc
        self.index = []
        self.span = 1 + ival * (k - 1)
        for i in range(len(t) - self.span + 1):  # for each subseq
            self.index.append((t[i:i+self.span:ival], i))  # add (subseq, offset)
        self.index.sort()  # alphabetize by subseq
    
    def query(self, p):
        """ Return index hits for first subseq of p """
        subseq = p[:self.span:self.ival]  # query with first subseq
        i = bisect.bisect_left(self.index, (subseq, -1))  # binary search
        hits = []
        while i < len(self.index):  # collect matching index entries
            if self.index[i][0] != subseq:
                break
            hits.append(self.index[i][1])
            i += 1
        return hits




def find2(p, genome_index, genome, max_error = 2):
    k = 8
    n = 24

    p1 = p[0:]
    p2 = p[1:]
    p3 = p[2:]

    p1_matches = genome_index.query(p1)
    print(f"p1 hits: {len(p1_matches)}")
    p2_matches = genome_index.query(p2)
    print(f"p3 hits: {len(p2_matches)}")
    p3_matches = genome_index.query(p3)
    print(f"p3 hits: {len(p3_matches)}")

    matches = set()

    for p1_match in p1_matches:
        if p1_match + n >= len(genome):
            continue
        if hamming_distance(genome[p1_match: p1_match + n], p) <= max_error:
            matches.add(p1_match)
    
    for p2_match in p2_matches:
        if p2_match -1 + n >= len(genome) or p2_match - 1 < 0:
            continue
        if hamming_distance(genome[p2_match - 1: p2_match -1 + n], p) <= max_error:
            matches.add(p2_match-1)
    
    for p3_match in p3_matches:
        if p3_match -2 + n >= len(genome) or p3_match - 2 < 0:
            continue
        if hamming_distance(genome[p3_match - 2: p3_match -2 + n], p) <= max_error:
            matches.add(p3_match-2)
    
    return matches

p = 'GGCGCGGTGGCTCACGCCTGTAAT'
ind = SubseqIndex(genome, 8, 3)
print(ind.index)
len(p)
o = find2(p, ind, genome)
len(o)
ind.query('CGGTCCTT')
