

## Array Attribute 
import numpy as np 

a1 =np.arange(5)
a2 = np.arange(12).reshape(3, 4)
# The first dimension has 2 subarrays.
# Each subarray has 3 rows and 2 columns.
a3 = np.arange(12).reshape(2, 3, 2)
# print(a1)
# print(a2)
# print(a3)

# number of dimension
# how many dimension of array  
# print(a1.ndim)




# shape 
# how many item preasent in a1 array not calculate wise 
# print(a1.shape)
# print(a2.shape)
# print(a3.shape)



# size 
# how many item present in array in calculate wise 
# print(a1.size)
# print(a2.size)
# print(a3.size)


# itemsize 
# how many mamory consume the array in biytes 
# print(a1.itemsize)
# print(a2.itemsize)
# print(a3.itemsize)




## dtype 
## what is the type of array ex:- float, int
print(a1.dtype)
print(a2.dtype)
print(a3.dtype)