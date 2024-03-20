

## Array Function 
import numpy as np 


###### argmax  ########
# np.argmax
# The numpy.argmax() function returns indices of the max element of the array in a particular axis.

# https://numpy.org/doc/stable/reference/generated/numpy.argmax.html

a = np.random.randint(1,100,15)
print(a)
print(np.argmax(a))    # output is 6 -> 6 number index per item hai jo sabse bada hai 
print(np.argmin(a))



