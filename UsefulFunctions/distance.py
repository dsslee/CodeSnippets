# Distance Related Function

import math
import numpy as np
from scipy.spatial import distance

# ===== EUCLIDEAN DISTANCE ====
# numpy version
def euclidean_distance_np(x, xhat):
    euc_distance = np.linalg.norm(x - xhat)
    return euc_distance

# scipy version
def euclidean_distance(x, xhat):
    diff = []
    for i in range(x.shape[0]):
        diff.append(distance.euclidean(x[i], xhat[i]))
    return np.array(diff)

# scipy version square euclidean 
def euclidean_distance_squared(x, xhat):
    diff = []
    for i in range(x.shape[0]):
        diff.append((distance.euclidean(x[i], xhat[i]))**2)
    return np.array(diff)


# GIVEN
x = np.array([[2, -1]])
xhat = np.array([[-2,2]])

# EXAMPLE WITH NUMPY
print("numpy version: ", euclidean_distance_np(x,xhat))

#EXAMPLE WITH SCIPY
print("scipy version: ", euclidean_distance(x,xhat))

#EXAMPLE WITH SCIPY SQUARED:
print("scipy version: ", euclidean_distance_squared(x,xhat))

def splitDataFrameList(df,target_column,separator):
    ''' df = dataframe to split,
    target_column = the column containing the values to split
    separator = the symbol used to perform the split
    returns: a dataframe with each entry for the target column separated, with each element moved into a new row. 
    The values in the other columns are duplicated across the newly divided rows.
    '''
    def splitListToRows(row,row_accumulator,target_column,separator):
        split_row = row[target_column].split(separator)
        for s in split_row:
            new_row = row.to_dict()
            new_row[target_column] = s
            row_accumulator.append(new_row)
    new_rows = []
    df.apply(splitListToRows,axis=1,args = (new_rows,target_column,separator))
    new_df = pd.DataFrame(new_rows)
    return new_df