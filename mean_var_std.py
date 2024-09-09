import numpy as np

def calculate(list):
    if (len(list) != 9):
        raise ValueError("List must contain nine numbers.")
    
    num = np.array(list)
    print(num)  

    mean_col = ([num[[0,3,6]].mean(), num[[1,4,7]].mean(), num[[2,5,8]].mean()])
    mean_row = [num[[0,1,2]].mean(), num[[3,4,5]].mean(), num[[6,7,8]].mean()]

    var_col = ([num[[0,3,6]].var(), num[[1,4,7]].var(), num[[2,5,8]].var()])
    var_row = [num[[0,1,2]].var(), num[[3,4,5]].var(), num[[6,7,8]].var()]

    std_col = ([num[[0,3,6]].std(), num[[1,4,7]].std(), num[[2,5,8]].std()])
    std_row = ([num[[0,1,2]].std(), num[[3,4,5]].std(), num[[6,7,8]].std()])

    max_col = ([num[[0,3,6]].max(), num[[1,4,7]].max(), num[[2,5,8]].max()])
    max_row = ([num[[0,1,2]].max(), num[[3,4,5]].max(), num[[6,7,8]].max()])

    min_col = ([num[[0,3,6]].min(), num[[1,4,7]].min(), num[[2,5,8]].min()])
    min_row = ([num[[0,1,2]].min(), num[[3,4,5]].min(), num[[6,7,8]].min()])

    sum_col = ([num[[0,3,6]].sum(), num[[1,4,7]].sum(), num[[2,5,8]].sum()])
    sum_row = ([num[[0,1,2]].sum(), num[[3,4,5]].sum(), num[[6,7,8]].sum()])
   


    return {
        'mean': [mean_col, mean_row, num.mean()],
    'variance': [var_col, var_row, num.var()],
    'standard deviation': [std_col, std_row, num.std()],
    'max': [max_col, max_row, num.max()],
    'min': [min_col,min_row, num.min()],
    'sum': [sum_col, sum_row, num.sum()]

    }
    