import numpy as np 


## Array Function 
# np.cumsum
# numpy.cumsum() function is used when we want to compute the cumulative sum of array elements over a given axis.

# https://numpy.org/doc/stable/reference/generated/numpy.cumsum.html




a = np.random.randint(1,100,15)


print(np.cumsum(a))   # sum of each index 
print(np.cumprod(a))   # multply of each index
