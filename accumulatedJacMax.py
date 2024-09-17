def compute_jacmax(Ti, Tj, top_k):
    '''
    Computes the JaccardMax value between two ranked lists Ti and Tj
    '''
    set_Ti = set()
    set_Tj = set()
    
    jaccard_max = 0
    for d in range(1, top_k):
        set_Ti.add(Ti[d-1])
        set_Tj.add(Tj[d-1])
        
        intersect = len(set_Ti & set_Tj)
        union = len(set_Ti | set_Tj)
        
        jaccard = intersect / union
        if jaccard == 1:
            return jaccard
        if jaccard > jaccard_max:
            jaccard_max = jaccard
            
    return jaccard_max

def compute_accumulated_jacmax(ranked_lists, index, top_k, alpha):
    '''
    Computes the Accumulated JaccardMax value for a query Ti
    '''
    Ti = ranked_lists[index]
    score = 0
    corr = 0
    for i in range(0, top_k):
        Tj = ranked_lists[int(Ti[i])]
        corr = compute_jacmax(Ti, Tj, top_k)
        score += corr * pow(alpha, i)

    return score / top_k