

## Array Function 
import numpy as np 


a1 = np.arange(12).reshape(4, 3)
a2 = np.arange(12, 24).reshape(3, 4)
a3 = np.arange(8).reshape(2, 2, 2)
print(a2)

### spliting 
## this is oposite of stacking 
print(np.hsplit(a2, 2))   # how many parts -> 2 parts

# vertical spliting 
print(np.vsplit(a1, 2))