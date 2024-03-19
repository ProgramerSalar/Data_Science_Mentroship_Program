

## Array Function 
import numpy as np 


a1 = np.arange(12)
a2 = np.arange(12, 24).reshape(4, 3)
a3 = np.arange(8).reshape(2, 2, 2)
# print(a3)


### Reshaping 


# Transponse 
print(a2)   # [4, 3]
print(a2.transpose())   # convert to [3, 4]
print(a2.T)  # easy way to Transpose 


# ravel 
print(a2.ravel())  # any dimension array convert to 1D array 

