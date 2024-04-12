# How to iterate over the Columns of a NumPy Array

import numpy as np

arr = np.array([
    [1, 3, 5, 7],
    [2, 4, 6, 8],
    [3, 5, 7, 9],
])

for column in arr.T:
    print(column)

    print('-' * 50)