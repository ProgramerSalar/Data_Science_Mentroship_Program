

## Array Function 
import numpy as np 


####### sort #############
# arrange the index in order wise ascending order/ descending order 


# np.sort
# Return a sorted copy of an array.

# https://numpy.org/doc/stable/reference/generated/numpy.sort.html



a = np.random.randint(1, 100, 15)
# print(a)
b = np.random.randint(1, 100, 24).reshape(6, 4)
print(b)


# ascending order
print(np.sort(a))
# descending order 
print(np.sort(a)[::-1])

# 2D sorting in colum wise 
print(np.sort(b, axis=0))   # axis 0 mins ->  column wise 
print(np.sort(b, axis=1))   # row wise sorting 


