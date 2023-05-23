
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






