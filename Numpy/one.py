import numpy as np 

# a = np.array([1,2,3])
# print(a)

# # 2D array || matrix
# a1 = np.array([[1, 2, 3],[4, 5, 6]])
# print(a1)


# # 3D array || Tensor 
# a2 = np.array([[[1, 2],[3, 4]], [[5, 6], [7, 8]]])
# print(a2)


# # dType 
# b = np.array([1, 2, 3], dtype=float)
# b1 = np.array([1, 2, 3], dtype=bool)
# b2 = np.array([1, 2, 3], dtype=complex)

# print(b)
# print(b1)
# print(b2)



# c = np.arange(10)  # range method in numpy is arange 
# c1 = np.arange(1, 10, 2)
# print(c1)
# print(c)



# shape method 
# c2 = np.arange(10).reshape(5, 2)  # 5 rows 2 column
# print(c2)


# every item is one 
# c3 = np.ones((2, 3))  # 2 rows 3 column
# print(c3)

# c4 = np.zeros((2, 3))
# print(c4)

# c5 = np.random.random((2, 3))
# print(c5)



# linspace
# (1, 10) means = range || 1 se 10 tak number
# 10 means = 10 number print kar ke do 
# means 1 se 10 tak 10 number print kar ke do 
# c6 = np.linspace(1, 10, 10)   # (lowerRange, upperRange, no_of_items_generate)
# print(c6) 


# identity 
# if you create 3 index of matrix then use identity method 
# 3 is index of matrix 
# in this matrix digonal items are 1 and other items is 0 
# like this:
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

c1 = np.identity(3)
print(c1)
