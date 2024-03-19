

## Array Attribute 
import numpy as np 

a1 =np.arange(5)
a2 = np.arange(12).reshape(3, 4)
# The first dimension has 2 subarrays.
# Each subarray has 3 rows and 2 columns.
a3 = np.arange(12, dtype=float).reshape(2, 3, 2)
# print(a1)
# print(a2)
# print(a3)



## changing datatype 
## a3 data Type is float but not dataType is int32
## what is the need of this things: if you change the dataType then you reduce the consume of mamery pawer 
print(a3.astype(np.int32))


