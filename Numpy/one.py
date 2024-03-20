

## Array Function 
import numpy as np 


###### concatenate ########
# np.concatenate
# numpy.concatenate() function concatenate a sequence of arrays along an existing axis.

# https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html


a = np.arange(6).reshape(2, 3)
b = np.arange(6, 12).reshape(2, 3)

c = np.concatenate((a, b), axis=0)
print(c)
d = np.concatenate((a, b), axis=1)    
print(d)




