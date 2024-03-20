

## Array Function 
import numpy as np 



## Advance Indexing 
a = np.arange(24).reshape(6, 4)
print(a)


### Fancy Indexing 

# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]
#  [16 17 18 19]
#  [20 21 22 23]]
# i want to 1 row 2, 4, 5
print(a[[1, 2, 4, 5]])

# i want to 0, 1 and 3 column 
print(a[:,[0, 1, 3]])  # : -> all row and column


### Boolean Indexing 

