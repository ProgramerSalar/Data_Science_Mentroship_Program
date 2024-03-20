

## Array Function 
import numpy as np 


###### where  ########
# np.where
# The numpy.where() function returns the indices of elements in an input array where the given condition is satisfied.

# https://numpy.org/doc/stable/reference/generated/numpy.where.html


a = np.random.randint(1,100,15)

# print(np.where(a > 50))


# replace all item is greater than 50 and 0 

# b = np.where(condition, true, false)  # if condition is true then do that else do that 
b = np.where(a > 50, 0, a)
print(b)





