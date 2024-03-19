

## Array Function 
import numpy as np 


a1 = np.arange(12)
a2 = np.arange(12, 24).reshape(4, 3)
a3 = np.arange(8).reshape(2, 2, 2)
# print(a3)


### Iterating 


# 1D array 
for i in a1:
    print(i)


# 2D array 
for i in a2:  # ek bar me ek row print hota, jab 2d me loop chalate ho
    print(i)
    
    
    
# 3D array 
for i in a3:   # ek bar me ek 2D array print hota hai 
    print(i)
    
    
# how to print 1D array in 3d data 
for i in np.nditer(a3): 
    print(i)