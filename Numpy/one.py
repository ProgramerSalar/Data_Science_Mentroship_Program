import numpy as np 


## Array Function 
# np.percentile
# numpy.percentile()function used to compute the nth percentile of the given data (array elements) along the specified axis.

# https://numpy.org/doc/stable/reference/generated/numpy.percentile.html




a = np.random.randint(1,100,15)
print(a)
print(np.percentile(a, 50))
print(np.percentile(a, 90))  # 90 -> 90 percentile par kon sa number ha 

print(np.median(a))
