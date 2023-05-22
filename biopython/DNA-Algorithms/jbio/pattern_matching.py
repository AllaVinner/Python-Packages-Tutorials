
def naive_exact_matching(p, t):
    occurrences = []
    for i in range(len(t) - len(p) + 1):  # loop over alignments
        match = True
        for j in range(len(p)):  # loop over characters
            char_checks += 1
            if t[i+j] != p[j]:  # compare characters
                match = False
                break
        if match:
            occurrences.append(i)  # all chars matched; record
    return occurrences

def boyer_more(p, p_bm, t):
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








