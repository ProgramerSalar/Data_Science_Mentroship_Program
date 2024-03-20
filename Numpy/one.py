

## Array Function 
import numpy as np 


## Brodcasting 
# The term broadcasting describes how NumPy treats arrays with different shapes during arithmetic operations.
# The smaller array is “broadcast” across the larger array so that they have compatible shapes.


# same shape 
# a = np.arange(6).reshape(3, 2)
# # print(a)
# b = np.arange(6, 12).reshape(3, 2)
# # print(b)
# print(a + b)


# different shape 
# diff shape
# a = np.arange(6).reshape(2,3)
# b = np.arange(3).reshape(1,3)

# print(a)
# print(b)

# print(a+b)

# Example 
# More examples

# a = np.arange(12).reshape(4,3)
# b = np.arange(3)

# print(a)
# print(b)

# print(a+b)


# a = np.arange(12).reshape(3,4)
# b = np.arange(3)

# print(a)
# print(b)

# print(a+b)


a = np.arange(3).reshape(1,3)
b = np.arange(3).reshape(3,1)

print(a)
print(b)

print(a+b)


a = np.arange(3).reshape(1,3)
b = np.arange(4).reshape(4,1)

print(a)
print(b)

print(a + b)


a = np.array([1])
# shape -> (1,1)
b = np.arange(4).reshape(2,2)
# shape -> (2,2)

print(a)
print(b)

print(a+b)


a = np.arange(12).reshape(3,4)
b = np.arange(12).reshape(4,3)

print(a)
print(b)

print(a+b)

a = np.arange(16).reshape(4,4)
b = np.arange(4).reshape(2,2)

print(a)
print(b)

print(a+b)