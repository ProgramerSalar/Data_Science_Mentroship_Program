

## Array Function 
import numpy as np 


###### Expend dimension ########
# np.expand_dims
# With the help of Numpy.expand_dims() method, we can get the expanded dimensions of an array

# https://numpy.org/doc/stable/reference/generated/numpy.expand_dims.html


a = np.arange(24)
# print(a)

b = np.expand_dims(a, axis=0)
print(b)
print(b.shape)

c = np.expand_dims(a, axis=1)
print(c.shape)



