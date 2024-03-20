

## Array Function 
import numpy as np 



## Advance Indexing 
a = np.arange(240)
# print(a)


### Fancy Indexing 

# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]
#  [16 17 18 19]
#  [20 21 22 23]]



### Boolean Indexing 

# find all number is greter than 50 
print(a[a > 50])


# find the even number
print(a[a % 2 == 0])


# find the even number and greter than 50 
b = a[(a > 50) & (a % 2 == 0)]
print(b)


# find the all number not divisible by 6
b1 = a[~(a % 2 == 0)]   # ~ -> not divisible by 2 
print(b1)

