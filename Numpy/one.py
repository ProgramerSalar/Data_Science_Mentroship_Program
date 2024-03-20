

## Array Function 
import numpy as np 


###### append ########
# np.append
# The numpy.append() appends values along the mentioned axis at the end of the array
# https://numpy.org/doc/stable/reference/generated/numpy.append.html




a = np.arange(20)
a2 = np.arange(24).reshape(6, 4)
# print(a)
print(a2)

# print(np.append(a, 200))
b = np.append(a2,np.random.random((a2.shape[0],1)),axis=1)   # axis=1 -> column wise 
print(b)