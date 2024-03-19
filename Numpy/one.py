

## Array Function 
import numpy as np 


a1 = np.random.random((3, 3))
# print(a1)


# 0 -> col || 1 -> row 
# print(np.max(a1, axis=0))   # colum wise maximum number 


# mean/median/std/var   # std -> standard daviation # var -> variance 
print(np.mean(a1))
print(np.median(a1))
print(np.std(a1))
print(np.var(a1))