import numpy as np 


## Array Function 
# np.corrcoef
# Return Pearson product-moment correlation coefficients.

# https://numpy.org/doc/stable/reference/generated/numpy.corrcoef.html




salary = np.array([20000,40000,25000,35000,60000])
experience = np.array([1,3,2,4,2])

print(np.corrcoef(salary,experience))

# output :- 
# [[1.         0.25344572]
#  [0.25344572 1.        ]]

# 0.25 ka relation hai 