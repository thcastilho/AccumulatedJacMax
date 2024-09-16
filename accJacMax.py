# Importing pyUDLF
import pyUDLF
from pyUDLF.utils import evaluation as ev
from pyUDLF.utils import readData as rd

import math

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

if __name__ == "__main__":
    # pyUDLF params
    pN = 1360 # dataset size
    pListFile =         'datasets/oxford17flowers/flowers_lists.txt' # list file
    pClassesFile =      'datasets/oxford17flowers/flowers_classes.txt' # classes file
    rk_file_path = 'datasets/oxford17flowers/ranked_lists/CNN-ResNet.txt' # ranked list file

    # Reading classes list
    class_list = rd.read_classes(pListFile, pClassesFile)

    # Reading ranked lists
    rks = rd.read_ranked_lists_file_numeric(rk_file_path)

    # Computing MAP measure
    map, map_list = ev.compute_map(rks, class_list)

    # Accumulated JaccardMax params
    index = 0
    k = 80
    alpha = 0.95

    accJacMax = compute_accumulated_jacmax(ranked_lists=rks, index=0, top_k=k, alpha=alpha)

    print(f'MAP value for image index {index}: {map_list[index]}')
    print(f'Accumulated JaccardMax value for image index {index}: {accJacMax}')