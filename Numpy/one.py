

## Array Function 
import numpy as np 


a1 = np.arange(12).reshape(3, 4)
a2 = np.arange(12, 24).reshape(4, 3)
a3 = np.arange(8).reshape(2, 2, 2)
# print(a3)

# print(a1)
# print(a2)


## Indexing and Slicing 
## indexing -> ek bar me ek hi item ko fetch karte hai 
## Slicing -> ek bar me multiple item ko nikal sakte ho 
print(a2)
print(a2[1, 2])   # 1st row and 2 -> column 

print(a3)
print(a3[1, 0, 1])   # 1 -> kon sa 2d array || 0 -> row || 1 -> col

