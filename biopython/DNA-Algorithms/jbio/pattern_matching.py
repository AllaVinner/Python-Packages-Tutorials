
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


def naive_haming_match(p, t, max_error = 2):
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


def naive_leniant_match(p, t, distance_fun, max_error = 2):
    occurrences = []
    for i in range(len(t) - len(p) + 1):  # loop over alignments
        if distance_fun(t[i:i+len(p)], p) <= max_error: 
            occurrences.append(i)
    return occurrences

def naive_leniant_best_match(p, t, distance_fun, keep: int = 1):
    best_matches = []
    best_scores = []
    for i in range(min(keep, len(t) - len(p) + 1)):
        best_matches.append(t[i:i+len(p)])
        best_scores.append(distance_fun(t[i:i+len(p)], p))
        
    for i in range(keep, len(t) - len(p) + 1):  # loop over alignments
        min_val = min(best_scores)
        score = distance_fun(t[i:i+len(p)], p)
        if score < min_val:
            min_index = best_scores.index(min_val)
            best_scores.pop(min_index)
            best_matches.pop(min_index)
            best_matches.append(i)
            best_scores.append(score)

    return best_matches, best_scores



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





def overlap(a, b, min_length=3):
    """ Return length of longest suffix of 'a' matching
        a prefix of 'b' that is at least 'min_length'
        characters long.  If no such overlap exists,
        return 0. """
    start = 0  # start all the way at the left
    while True:
        start = a.find(b[:min_length], start)  # look for b's prefix in a
        if start == -1:  # no more occurrences to right
            return 0
        # found occurrence; check for full suffix/prefix match
        if b.startswith(a[start:]):
            return len(a)-start
        start += 1  # move just past previous match


import itertools

def scs(ss):
    """ Returns shortest common superstring of given
        strings, which must be the same length """
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
    return shortest_sup  # return shortest
