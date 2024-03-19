

## Array Function 
import numpy as np 


a1 = np.arange(12).reshape(3, 4)
a2 = np.arange(12, 24).reshape(4, 3)

# print(a1)
# print(a2)



## dot product 
# print(np.dot(a1, a2))



## log and exponent 
# print(np.log(a1))
# print(np.exp(a1))



## round/floor/ceil 
b = 1.2
b1 = 1.6 

print(np.round(b))
print(np.floor(b))
print(np.floor(b1))  # output -> 1 
print(np.ceil(b1))   # output -> 2 
print(np.ceil(b))