

## Array Function 
import numpy as np 


a1 = np.arange(12).reshape(4, 3)
a2 = np.arange(12, 24).reshape(4, 3)
a3 = np.arange(8).reshape(2, 2, 2)
# print(a1)

### Stacking 

# how to add horizontal array add in 2D, 3D
print(np.hstack((a1, a2)))

# vertival add 
print(np.vstack((a1, a2)))