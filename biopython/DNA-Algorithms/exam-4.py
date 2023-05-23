

#Q1 11

ss = ['CCT', 'CTT', 'TGC', 'TGG', 'GAT', 'ATT']
sss = scs(ss)
len(sss)

# Q2  5, 2, 5 (not the right answerw)
def scs_with_stats(ss):
    """ Returns shortest common superstring of given
        strings, which must be the same length 
    """
    solutions = []
    shortest_sup = None
    for ssperm in itertools.permutations(ss):
        sup = ssperm[0]  # superstring starts as first string
        for i in range(len(ss)-1):
            # overlap adjacent strings A and B in the permutation
            olen = overlap(ssperm[i], ssperm[i+1], min_length=1)
            # add non-overlapping portion of B to superstring
            sup += ssperm[i+1][olen:]
        if shortest_sup is None or len(sup) < len(shortest_sup):
            shortest_sup = sup  # found shorter superstring
            num_solutions = [shortest_sup]
        if shortest_sup is not None and len(sup) == len(shortest_sup):
            solutions.append(sup)
        
    return shortest_sup, solutions  # return shortest

ans, num = scs_with_stats(ss)
ans
set(num)


# Q3 4633
reads, quals = readFastq('./biopython/data/ads1_week4_reads.fq')
k = 20

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

def get_greedy_pair(reads, k):
    best_overlap = 0
    best_pair = None

    kk = k
    while True:
        rels = create_kmer_relations(reads, kk)
        for base_i, base_read in enumerate(reads):
            suffix = base_read[-kk:]
            for compare_read_i in rels[suffix]:
                if base_i == compare_read_i:
                    continue
                compare_read = reads[compare_read_i]
                ovelap_score = overlap(base_read, compare_read, min_length=kk)
                if ovelap_score > best_overlap:
                    best_overlap = ovelap_score
                    best_pair = (base_i, compare_read_i)
        if best_pair is None:
            kk -= 1
        else:
            break
    return best_pair, best_overlap



def greedy_scs(ss, k= 20):
    merge_indeces = [[i] for i in range(len(ss))]
    merge_reads = ss.copy()
    for iter in range(len(ss)-1):
        (src, dst), overlap_score = get_greedy_pair(merge_reads, k)
        print(src, dst)
        if src > dst:
            src_i = merge_indeces.pop(src)
            dst_i = merge_indeces.pop(dst)
            src_read = merge_reads.pop(src)
            dst_read = merge_reads.pop(dst)
        else:
            dst_i = merge_indeces.pop(dst)
            src_i = merge_indeces.pop(src)
            dst_read = merge_reads.pop(dst)
            src_read = merge_reads.pop(src)

        merge_indeces.append(src_i + dst_i)
        merge_reads.append(src_read + dst_read[overlap_score:])
        print(iter)
    return merge_reads, merge_indeces

ss = 'aafklalfhskhejuncskdnvdkialskdjflsdfkhjdknkdfjhskfhjdhkaksdfkajshdfkakwhkjweriqyeiryakdbvkjshkjbxmsdfsmnndkfnsldknf'
n = 13
d = int( len(ss)/(2*n+3))+1
r = [ss[i*2*d: i*2*d+3*d] for i in range(n)]
r

re_s, ii = greedy_scs(r, 4)
re_s[0] == ss[:len(re_s[0])]
len(re_s[0])
len(ss)

rere, reii = greedy_scs(reads, k)

greedy_scs(r, 4)



reconstructed = rere[0]
len(reconstructed)


reconstructed.count('A')

# Q4 3723
reconstructed.count('T')


