

## Array Function 
import numpy as np 


### NUMPY ARRAY VS PYTHON LISTS 

# speed for List 
# speed
# list
# a = [i for i in range(10000000)]
# b = [i for i in range(10000000,20000000)]

# c = []
# import time 

# start = time.time()
# for i in range(len(a)):
#   c.append(a[i] + b[i])
# print(time.time()-start)
    
    
    
# speed for list 
# numpy
# import numpy as np
# a = np.arange(10000000)
# b = np.arange(10000000,20000000)

# start = time.time()
# c = a + b
# print(time.time()-start)


import sys 

e = [i for i in range(10000000)]
print(sys.getsizeof(e))


e2 = np.arange(10000000)
print(sys.getsizeof(e2))

