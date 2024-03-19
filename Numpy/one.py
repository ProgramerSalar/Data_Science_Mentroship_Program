

## Array Function 
import numpy as np 


a1 = np.arange(12)
a2 = np.arange(12, 24).reshape(4, 3)
a3 = np.arange(8).reshape(2, 2, 2)
# print(a3)

# print(a1)
# print(a2)


## Indexing and Slicing 
## indexing -> ek bar me ek hi item ko fetch karte hai 
## Slicing -> ek bar me multiple item ko nikal sakte ho 
# print(a2)
# print(a2[1, 2])   # 1st row and 2 -> column 

# print(a3)
# print(a3[1, 0, 1])   # 1 -> kon sa 2d array || 0 -> row || 1 -> col



# Slicing 
# print(a1[1:3])   # 1 or 2 print hot || 1 is minimum number 3 is maximum number
# print(a1[1:5:2])   # 1 or 2 print hot || 1 is minimum number 5 is maximum number  || jo 2 se divisible hoga oo nahi ayega 
# print(a2[0, :])    # 0 se sare column chahiye 

# how to calculate 3 column in a2 
# print(a2[:, 2])

# [[12 13 14]
#  [15 16 17]
#  [18 19 20]
#  [21 22 23]]

# i should 16, 19, 22 
# print(a2[1:, 1:2])  

# i should 12, 14, 21, 23 
print(a2[::3, 0::2])


