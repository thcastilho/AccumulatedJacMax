# Importing pyUDLF
import pyUDLF
from pyUDLF.utils import evaluation as ev
from pyUDLF.utils import readData as rd

# Importing Accumulated JaccardMax function
from accumulatedJacMax import compute_accumulated_jacmax

# Importing correlation function from sciPy library
from scipy.stats import pearsonr

if __name__ == "__main__":
    # pyUDLF params
    pN           = 1360 # dataset size
    pListFile    = 'datasets/oxford17flowers/flowers_lists.txt' # list file
    pClassesFile = 'datasets/oxford17flowers/flowers_classes.txt' # classes file
    rk_file_path = 'datasets/oxford17flowers/ranked_lists/CNN-ResNet.txt' # ranked list file

    # Reading classes list
    class_list = rd.read_classes(pListFile, pClassesFile)

    # Reading ranked lists
    rks = rd.read_ranked_lists_file_numeric(rk_file_path)

    # Computing MAP measure
    map, map_list = ev.compute_map(rks, class_list)

    # Accumulated JaccardMax params
    k = 80
    alpha = 0.95

    # Computing Acc. JaccardMax values
    accjacmax_values = []
    for i in range(pN):
        accjacmax_values.append(compute_accumulated_jacmax(ranked_lists=rks, index=i, top_k=k, alpha=alpha))

    pearson_corr = pearsonr(map_list, accjacmax_values)

    print(f'Correlation between MAP measure and Acc. JaccardMax: {round(pearson_corr[0], 4)}')